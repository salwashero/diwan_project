// mobile_app/lib/services/api_service.dart
import 'package:http/http.dart' as http;
import '../models/poem.dart'; // استيراد نموذج القصيدة
import 'dart:convert'; // لاستخدام jsonDecode و utf8

class ApiService {
  // --- تم تحديث عنوان الـ API هنا ---
  // تم استخدام عنوان URL العام الذي يوفره Gitpod لسيرفر Django
  // الذي يعمل على المنفذ 8000 داخل نفس مساحة العمل.
  static String _baseUrl = "https://8000-salwashero-diwanproject-gqutfzbnnsm.ws-us118.gitpod.io/api/"; // <-- تم التحديث هنا

  // دالة لتحديث عنوان الـ API (يمكن استخدامها لاحقًا إذا لزم الأمر)
  static void setBaseUrl(String url) {
    // Ensure the URL ends with /api/
    if (!url.endsWith('/')) {
      url += '/';
    }
    if (!url.endsWith('api/')) {
      url += 'api/';
    }
    _baseUrl = url;
    print("API Base URL set to: $_baseUrl"); // للتحقق
  }

  // دالة جلب قائمة القصائد
  static Future<List<Poem>> fetchPoems() async {
    final String poemsUrl = '${_baseUrl}poems/'; // بناء الـ URL الكامل لنقطة نهاية القصائد
    print("Attempting to fetch poems from: $poemsUrl"); // للتحقق
    try {
      final response = await http.get(Uri.parse(poemsUrl));

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
        print("Response body: ${response.body}"); // طباعة الجسم في حالة الفشل
        throw Exception('Failed to load poems (Status code: ${response.statusCode})');
      }
    } catch (e) {
       print("Error fetching poems: $e"); // طباعة الخطأ للمساعدة
       // Consider specific error handling (e.g., network error, format error)
       if (e is http.ClientException) {
         throw Exception('Network error fetching poems: $e');
       } else {
         throw Exception('Error processing poems data: $e');
       }
    }
  }

  // --- الدوال الأخرى للإضافة والتعديل والحذف ستأتي هنا ---
  // مثال (غير مكتمل - يحتاج لمصادقة التوكن):
  /*
  static Future<Poem> createPoem(String title, String body, String token) async {
    final String poemsUrl = '${_baseUrl}poems/';
    final response = await http.post(
      Uri.parse(poemsUrl),
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
      print("Failed to create poem. Status: ${response.statusCode}");
      print("Response body: ${response.body}");
      throw Exception('Failed to create poem.');
    }
  }
  */
}