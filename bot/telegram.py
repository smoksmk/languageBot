from app.bot import bot
from app.db import session_scope
from models.controller import Dictionary


@bot.message_handler(commands=['word'])
def word(message):
    print(message.chat.id)
    with session_scope() as session:
        dictionary = Dictionary(session)
        level = dictionary.get_level('elementary')
        word = dictionary.get_random_word(level)
        word_ru = [i.name for i in word[1]]

        print(word[0], ", ".join(word_ru))
        mess = f"{word[0]}: {', '.join(word_ru)}"
    bot.send_message(message.chat.id, mess)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
