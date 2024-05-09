import asyncio
from telethon import TelegramClient
from instabot import Bot

# Настройки доступа к Telegram API
api_id = 'YOUR_TELEGRAM_API_ID'
api_hash = 'YOUR_TELEGRAM_API_HASH'
phone = 'YOUR_PHONE_NUMBER'
channel_username = 'YOUR_CHANNEL_USERNAME'

# Настройки доступа к Instagram API
insta_username = 'YOUR_INSTAGRAM_USERNAME'
insta_password = 'YOUR_INSTAGRAM_PASSWORD'

# Группы в Instagram, куда будет отправлен пост
instagram_groups = ['group1', 'group2', 'group3', 'group4', 'group5', 'group6', 'group7']

# Инициализация ботов
telegram_client = TelegramClient('session_name', api_id, api_hash)
bot = Bot()
bot.login(username=insta_username, password=insta_password)

# Получение и отправка поста
async def get_and_send_post_to_instagram():
    async with telegram_client:
        channel = await telegram_client.get_entity(channel_username)
        messages = await telegram_client.get_messages(channel, limit=1)
        for message in messages:
            if message.photo:  # Проверяем, есть ли в сообщении фотография
                # Получаем путь к фото
                photo_path = await message.download_media()
                post_text = f"{message.text}\n\nПодписывайтесь на канал в Telegram: t.me/{channel_username}"
                for group in instagram_groups:
                    try:
                        bot.upload_photo(photo_path, caption=post_text)
                        print(f"Пост успешно отправлен в группу {group} в Instagram")
                    except Exception as e:
                        print(f"Ошибка при отправке поста в группу {group} в Instagram:", e)
            else:
                print("Сообщение не содержит фотографии")

# Запуск скрипта
async def main():
    await telegram_client.start()
    await get_and_send_post_to_instagram()
    await telegram_client.disconnect()
    bot.logout()

asyncio.run(main())
