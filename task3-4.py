import telebot
import pyodbc
from datetime import datetime

bot_token = '6777734489:AAHpKiil-p7o09NV1lkZAa2HYGD8pLMhw6I'
bot = telebot.TeleBot(bot_token)

db_path = r'C:\Users\77083\Desktop\database tgbt\database_file.accdb'
connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_path};'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Отдельные операторы CREATE TABLE
cursor.execute('''
    CREATE TABLE Messages (
        TextMessage TEXT,
        SendDate DATETIME
    )
''')
conn.commit()

@bot.message_handler(func=lambda message: True)
def reply_to_all_messages(message):
    reply_text = f"Strattonbot + {message.text}"
    bot.send_message(message.chat.id, reply_text)

    insert_query = 'INSERT INTO Messages (TextMessage, SendDate) VALUES (?, ?)'
    try:
        cursor.execute(insert_query, (message.text, datetime.now()))
        conn.commit()
        print("Сообщение успешно добавлено в базу данных.")
    except Exception as e:
        print(f"Ошибка при записи в базу данных: {e}")

if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    finally:
        conn.close()
