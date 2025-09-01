from telegram.ext import Updater, MessageHandler, Filters

BOT_TOKEN = "7630187182:AAFHSwb5pYMJ8FKGt-2kTGyF5wEj5n2uxyM"

def save_file(update, context):
    file = update.message.document or update.message.video or update.message.audio
    if file:
        file_id = file.file_id
        new_file = context.bot.get_file(file_id)
        file_name = file.file_name if file.file_name else "unnamed_file"

        new_file.download(file_name)
        update.message.reply_text(f"✅ Saved {file_name}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.document | Filters.video | Filters.audio, save_file))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
