// mobile_app/lib/services/api_service.dart
import 'package:http/http.dart' as http;
import '../models/poem.dart'; // استيراد نموذج القصيدة
import 'dart:convert'; // لاستخدام jsonDecode و utf8

class ApiService {
  // --- !!! نقطة مهمة جداً: التعامل مع عنوان الـ API !!! ---
  // الخيار 1: تشغيل Django أيضاً في Gitpod (مُوصى به للسهولة الآن)
  //    - افتحي طرفية جديدة في Gitpod.
  //    - cd /workspace/diwan_project/backend (أو مسار الباك إند)
  //    - تأكدي من وجود requirements.txt، ثم pip install -r requirements.txt (أو تثبيت Django و DRF يدوياً)
  //    - شغلي السيرفر: python manage.py runserver 0.0.0.0:8000
  //    - Gitpod سيجعل المنفذ 8000 متاحاً ويعطيكِ URL خاص به (مثل https://8000-your-gitpod-workspace-id.ws-euXX.gitpod.io).
  //    - استخدمي هذا الـ URL الذي يظهر لكِ من Gitpod هنا في _baseUrl.
  //
  // الخيار 2: استخدام ngrok (إذا أردتِ إبقاء Django على جهازك المحلي)
  //    - تشغيل ngrok على جهازك المحلي: ngrok http 8000
  //    - سيعطيكِ ngrok عنوان https عام (مثل https://abcd-1234.ngrok.io).
  //    - استخدمي هذا العنوان العام هنا في _baseUrl.
  //
  // الخيار 3: استخدام العنوان المحلي المباشر (سيعمل فقط إذا شغلتِ Flutter على الويب من نفس الجهاز المحلي، أو على محاكي أندرويد على نفس الجهاز)
  //    -  "http://127.0.0.1:8000" للويب المحلي
  //    -  "http://10.0.2.2:8000" لمحاكي أندرويد الرسمي
  //
  // --- سنختار بنية الخيار 1 مبدئياً، لكن استبدلي الـ URL بالذي سيظهر لكِ عند تشغيل Django في Gitpod ---
  static String _baseUrl = "http://127.0.0.1:8000"; // <-- استبدليه لاحقاً بالـ URL الصحيح من Gitpod أو ngrok

  // دالة لتحديث عنوان الـ API (إذا استخدمنا طريقة ديناميكية)
  static void setBaseUrl(String url) {
    _baseUrl = url;
    print("API Base URL set to: $_baseUrl"); // للتحقق
  }

  // دالة جلب قائمة القصائد
  static Future<List<Poem>> fetchPoems() async {
    print("Attempting to fetch poems from: $_baseUrl/api/poems/"); // للتحقق
    try {
      final response = await http.get(Uri.parse('$_baseUrl/api/poems/'));

      print("API Response Status Code: ${response.statusCode}"); // للتحقق
      // print("API Response Body: ${utf8.decode(response.bodyBytes)}"); // للتحقق (قد يكون طويلاً)

      if (response.statusCode == 200) {
        final dynamic data = jsonDecode(utf8.decode(response.bodyBytes)); // استخدام utf8 لدعم العربية

        // التحقق إذا كانت البيانات قائمة مباشرة أو ضمن مفتاح 'results'
        if (data is List) {
          // قائمة مباشرة
          return List<Poem>.from(data.map((item) => Poem.fromJson(item)));
        } else if (data is Map<String, dynamic> && data.containsKey('results') && data['results'] is List) {
          // قائمة ضمن مفتاح 'results' (شائع في DRF Pagination)
          return List<Poem>.from(data['results'].map((item) => Poem.fromJson(item)));
        } else {
          // شكل بيانات غير متوقع
          print("Unexpected JSON format received.");
          throw Exception('Unexpected JSON format received.');
        }
      } else {
        print("Failed to load poems. Status code: ${response.statusCode}");
        throw Exception('Failed to load poems (Status code: ${response.statusCode})');
      }
    } catch (e) {
       print("Error fetching poems: $e"); // طباعة الخطأ للمساعدة
       throw Exception('Error fetching poems: $e');
    }
  }

  // --- الدوال الأخرى للإضافة والتعديل والحذف ستأتي هنا ---
  // مثال (غير مكتمل - يحتاج لمصادقة التوكن):
  /*
  static Future<Poem> createPoem(String title, String body, String token) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/api/poems/'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Token $token', // إرسال التوكن للمصادقة
      },
      body: jsonEncode(<String, String>{
        'title': title,
        'body': body,
      }),
    );

    if (response.statusCode == 201) { // 201 Created
      return Poem.fromJson(jsonDecode(utf8.decode(response.bodyBytes)));
    } else {
      throw Exception('Failed to create poem.');
    }
  }
  */
}