import 'package:flutter/material.dart';
import 'services/api_service.dart'; // تأكد من وجود هذا الملف
import 'models/poem.dart';      // تأكد من وجود هذا الملف

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ديوان الشاعر الرقمي',
      theme: ThemeData(
        primarySwatch: Colors.indigo, // اختر لوناً يناسبك
        visualDensity: VisualDensity.adaptivePlatformDensity,
        fontFamily: 'Tajawal', // مثال لاستخدام خط عربي إذا أضفته
      ),
      debugShowCheckedModeBanner: false, // لإخفاء شريط Debug
      home: const HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  late Future<List<Poem>> futurePoems;

  @override
  void initState() {
    super.initState();
    // استدعاء جلب القصائد عند بدء تشغيل الصفحة
    futurePoems = ApiService.fetchPoems();
  }

  // دالة لتحديث القائمة (يمكن استدعاؤها بعد إضافة/حذف)
  void _refreshPoems() {
    setState(() {
      futurePoems = ApiService.fetchPoems();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('القصائد'),
        actions: [
          // زر للتحديث اليدوي
          IconButton(
            icon: const Icon(Icons.refresh),
            onPressed: _refreshPoems,
            tooltip: 'تحديث القائمة',
          ),
        ],
      ),
      body: FutureBuilder<List<Poem>>(
        future: futurePoems,
        builder: (context, snapshot) {
          // حالة الانتظار
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          // حالة الخطأ
          else if (snapshot.hasError) {
            print("Error in FutureBuilder: ${snapshot.error}");
            print("Stack trace: ${snapshot.stackTrace}");
            return Center(
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Text(
                  'حدث خطأ أثناء تحميل القصائد:\n${snapshot.error}',
                  textAlign: TextAlign.center,
                  style: const TextStyle(color: Colors.red),
                ),
              ),
            );
          }
          // حالة وجود بيانات
          else if (snapshot.hasData) {
            final poems = snapshot.data!;
            // التحقق إذا كانت القائمة فارغة
            if (poems.isEmpty) {
              return const Center(child: Text('لا توجد قصائد لعرضها حالياً.'));
            }
            // عرض القائمة
            return ListView.builder(
              itemCount: poems.length,
              itemBuilder: (context, index) {
                final poem = poems[index];
                return ListTile(
                  title: Text(poem.title),
                  subtitle: Text(
                    poem.body.length > 100 ? '${poem.body.substring(0, 100)}...' : poem.body,
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                  ),
                  // يمكن إضافة onTap للانتقال لصفحة التفاصيل لاحقاً
                  onTap: () {
                    // Navigator.push(context, MaterialPageRoute(builder: (context) => PoemDetailPage(poem: poem)));
                    print('Selected poem: ${poem.title}'); // مؤقتًا
                  },
                );
              },
            );
          }
          // حالة غير متوقعة (لا يجب أن تحدث عادةً)
          else {
            return const Center(child: Text('حالة غير معروفة.'));
          }
        },
      ),
      // سنضيف زر الإضافة لاحقاً
      // floatingActionButton: FloatingActionButton(
      //   onPressed: () {
      //     // الانتقال لصفحة إضافة قصيدة
      //   },
      //   child: const Icon(Icons.add),
      //   tooltip: 'إضافة قصيدة جديدة',
      // ),
    );
  }
}