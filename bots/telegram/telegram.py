from app.bot import bot
from bots.telegram.utils import gen_keyboard, get_session


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    session = get_session(message.chat)
    item = session.get_item(message.text)
    markup = gen_keyboard(item.get_keyboard())
    result = item.get_message()
    if isinstance(result, list):
        for mess in result:
            bot.send_message(message.chat.id, mess, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, item.get_message(), reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)
