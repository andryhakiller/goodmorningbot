from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7895917870:AAEtFMKp1YWVhR6IbF7SLk3LREnq_L8ViyE"
YOUR_CHAT_ID = "1024602298"

async def start(update: Update, context: CallbackContext):
    user_name = update.message.from_user.first_name
    await update.message.reply_text(
        f"Привет, {user_name}! Меня создал Андрей, чтобы пожелать тебе доброго утра.\n"
        "Используй команду:\n"
        "/sendphrase — получить заслуженное доброе утро\n"
        "/sendmessage — помочь Андрею в пожеланиях"
    )

# Команда /sendphrase
async def send_phrase(update: Update, context: CallbackContext):
    user_name = update.message.from_user.first_name
    phrase = f"Привет, {user_name}! От всей души поздравляю тебя с добрым утром❤"
    await update.message.reply_text(phrase)

# Команда /sendmessage
async def send_message(update: Update, context: CallbackContext):
    await update.message.reply_text("Помоги с идеями для новых добрых утр")

# Обработка текстовых сообщений (для пересылки)
async def handle_text(update: Update, context: CallbackContext):
    user_message = update.message.text
    user_name = update.message.from_user.first_name
    await context.bot.send_message(
        chat_id=YOUR_CHAT_ID,
        text=f"Сообщение от пользователя {user_name}: {user_message}"
    )
    await update.message.reply_text("Ваше сообщение отправлено владельцу бота!")

# Основная функция
def main():
    # Инициализация бота
    application = Application.builder().token(TOKEN).build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("sendphrase", send_phrase))
    application.add_handler(CommandHandler("sendmessage", send_message))

    # Обработчик текстовых сообщений (для пересылки)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()