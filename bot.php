<?php
// التوكن الخاص بالبوت
$botToken = "7913260818:AAGT5rKbYr6RdKrO5O3OKmBKbSpsdSZ_Z5Y";

// الحصول على البيانات القادمة من Telegram
$update = file_get_contents("php://input");
$updateArray = json_decode($update, true);

// استخراج المعلومات الأساسية
$chatId = $updateArray['message']['chat']['id'];
$text = $updateArray['message']['text'];

// التحقق إذا كان المستخدم ضغط على /start
if ($text === "/start") {
    $message = "مرحبًا! اضغط على الرابط التالي للوصول إلى صفحة جمع البيانات:\n\n";
    $message .= "<a href='https://hanoybot.github.io/Data-collection/'>اضغط هنا</a>";

    // إرسال الرد إلى المستخدم
    file_get_contents("https://api.telegram.org/bot$botToken/sendMessage?chat_id=$chatId&text=" . urlencode($message) . "&parse_mode=HTML");
}
?>