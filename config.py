import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "898036971"))

COMPANY_NAME = os.getenv("COMPANY_NAME", "Lead Demo Bot")
CONTACT_USERNAME = os.getenv("CONTACT_USERNAME", "@yourusername")
LANGUAGE = os.getenv("LANGUAGE", "RU")

TEXTS = {
    "RU": {
        "start": f"Здравствуйте! Добро пожаловать в {COMPANY_NAME} 👋\n\nНажмите кнопку ниже, чтобы оставить заявку.",
        "button": "📝 Оставить заявку",
        "ask_name": "Введите ваше имя:",
        "ask_phone": "Введите ваш номер телефона:",
        "ask_service": "Какая услуга вас интересует?",
        "ask_comment": "Добавьте комментарий или напишите '-' если комментария нет.",
        "success": "Спасибо! Ваша заявка отправлена ✅\nС вами скоро свяжутся.",
        "cancel": "❌ Отмена",
        "cancel_text": "Заявка отменена.",
        "restart": "Вы можете начать заново, нажав кнопку ниже."
    },
    "EN": {
        "start": f"Welcome to {COMPANY_NAME} 👋\n\nPress the button below to leave a request.",
        "button": "📝 Leave a request",
        "ask_name": "Enter your name:",
        "ask_phone": "Enter your phone number:",
        "ask_service": "What service are you interested in?",
        "ask_comment": "Add a comment or type '-' if there is no comment.",
        "success": "Thank you! Your request has been sent ✅\nWe will contact you soon.",
        "cancel": "❌ Cancel",
        "cancel_text": "Request cancelled.",
        "restart": "You can start again by pressing the button below."
    }
}
