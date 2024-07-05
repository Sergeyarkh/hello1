import telebot

bot = telebot.TeleBot('7377001417:AAGZgcM24yPtxoVyft8Qe8nMZgS3gCPjjZ4')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hi!, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')




@bot.message_handler()
def get_user_text(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f"Твой ИД: {message.from_user.id}", parse_mode='html')
    elif message.text == 'photo':
        photo = open("IMG_1.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'LL':
        ll = open("Lebenslauf SA.pdf", "rb")
        bot.send_document(message.chat.id, ll)
    elif message.text == 'AB':
        ab = open("Arbeitsbuch.PDF", "rb")
        bot.send_document(message.chat.id, ab)




bot.polling(none_stop=True)