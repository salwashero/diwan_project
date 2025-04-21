// mobile_app/lib/models/poem.dart
import 'dart:convert';

// دالة مساعدة لتحويل قائمة JSON إلى قائمة Poem
List<Poem> poemFromJson(String str) => List<Poem>.from(json.decode(str).map((x) => Poem.fromJson(x)));

// دالة مساعدة لتحويل Poem واحد إلى JSON (قد نحتاجها لاحقاً للإرسال)
String poemToJson(Poem data) => json.encode(data.toJson());

class Poem {
    final int id;       // معرف القصيدة من قاعدة البيانات
    final String title;    // عنوان القصيدة
    final String body;     // نص القصيدة
    final int owner;    // معرف المستخدم المالك للقصيدة

    Poem({
        required this.id,
        required this.title,
        required this.body,
        required this.owner,
    });

    // Factory constructor لإنشاء كائن Poem من خريطة (Map) قادمة من JSON
    factory Poem.fromJson(Map<String, dynamic> json) => Poem(
        id: json["id"] ?? 0, // استخدام قيمة افتراضية 0 إذا كانت id غير موجودة (احتياطي)
        title: json["title"] ?? "", // استخدام قيمة افتراضية إذا كان العنوان غير موجود
        body: json["body"] ?? "", // استخدام قيمة افتراضية إذا كان النص غير موجود
        owner: json["owner"] ?? 0, // استخدام قيمة افتراضية إذا كان المالك غير موجود
    );

    // دالة لتحويل كائن Poem إلى خريطة (Map) لإرسالها كـ JSON
    Map<String, dynamic> toJson() => {
        "id": id,
        "title": title,
        "body": body,
        "owner": owner,
    };
}