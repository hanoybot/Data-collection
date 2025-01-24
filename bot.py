from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# بيانات البوت
BOT_TOKEN = "7782026361:AAHmzG4VaYRFrVMxdNLH8K7nGkLGPwIr7pY"

# دالة الاستجابة للأمر "/start"
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message = "مرحبًا! هذا هو الرابط الخاص بك:\n\nhttps://hanoybot.github.io/Data-collection/"
    await context.bot.send_message(chat_id=chat_id, text=message)

def main():
    # إنشاء تطبيق البوت
    application = Application.builder().token(BOT_TOKEN).build()

    # إضافة أمر "/start"
    application.add_handler(CommandHandler("start", start_command))

    # بدء تشغيل البوت
    print("البوت يعمل الآن!")
    application.run_polling()

if __name__ == "__main__":
    main()
