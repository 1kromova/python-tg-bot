import python-telegram-bot
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Определяем состояния разговоров
SELLER, BUYER, ASK_SELLER_REGION, ASK_SELLER_PRODUCTS, ASK_SELLER_PHONE, ASK_BUYER_REGION, ASK_BUYER_AMOUNT, ASK_BUYER_PHONE = range(8)

def start(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Продавец', 'Закупщик']]

    update.message.reply_text(
        'Привет! Я бот для покупок и продаж. Выберите свою роль:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    
    return SELLER

def seller(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Кто вы?')
    return ASK_SELLER_REGION

def ask_seller_region(update: Update, context: CallbackContext) -> int:
    context.user_data['seller_name'] = update.message.text
    update.message.reply_text('С какого региона вы?')
    return ASK_SELLER_PRODUCTS

def ask_seller_products(update: Update, context: CallbackContext) -> int:
    context.user_data['seller_region'] = update.message.text
    update.message.reply_text('Сколько у вас продукции?')
    return ASK_SELLER_PHONE

def ask_seller_phone(update: Update, context: CallbackContext) -> int:
    context.user_data['seller_products'] = update.message.text
    update.message.reply_text('Ваш номер телефона:')
    return ConversationHandler.END

def buyer(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Кто вы?')
    return ASK_BUYER_REGION

def ask_buyer_region(update: Update, context: CallbackContext) -> int:
    context.user_data['buyer_name'] = update.message.text
    update.message.reply_text('С какого региона вы?')
    return ASK_BUYER_AMOUNT

def ask_buyer_amount(update: Update, context: CallbackContext) -> int:
    context.user_data['buyer_region'] = update.message.text
    update.message.reply_text('Сколько продукции вы бы хотели купить?')
    return ASK_BUYER_PHONE

def ask_buyer_phone(update: Update, context: CallbackContext) -> int:
    context.user_data['buyer_amount'] = update.message.text
    update.message.reply_text('Ваш номер телефона:')
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Разговор отменен.')
    return ConversationHandler.END

def main() -> None:
    updater = Updater('7356728417:AAH-LubJZlyJBWYbbuDWPS-gKS_5158uZVI
')
    
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELLER: [MessageHandler(Filters.regex('^(Продавец)$'), seller),
                     MessageHandler(Filters.regex('^(Закупщик)$'), buyer)],
                     
            ASK_SELLER_REGION: [MessageHandler(Filters.text & ~Filters.command, ask_seller_region)],
            ASK_SELLER_PRODUCTS: [MessageHandler(Filters.text & ~Filters.command, ask_seller_products)],
            ASK_SELLER_PHONE: [MessageHandler(Filters.text & ~Filters.command, ask_seller_phone)],

            ASK_BUYER_REGION: [MessageHandler(Filters.text & ~Filters.command, ask_buyer_region)],
            ASK_BUYER_AMOUNT: [MessageHandler(Filters.text & ~Filters.command, ask_buyer_amount)],
            ASK_BUYER_PHONE: [MessageHandler(Filters.text & ~Filters.command, ask_buyer_phone)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```

# 3. Замените `'YOUR TOKEN HERE'` на токен вашего бота, который можно получить у [BotFather](https://core.telegram.org/bots#botfather).

# 4. Запустите скрипт:
# ```bash
# python telegram_bot.py
# ```

# Теперь ваш Telegram-бот должен быть активен и задавать пользователям соответствующие вопросы в зависимости от их роли (продавец или закупщик).
```bash
python telegram_bot.py
```
