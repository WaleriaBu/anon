@dp.message()
async def anon_forward(message: Message):
    user_id = message.from_user.id
    now = asyncio.get_event_loop().time()

    if user_id in last_message_time and now - last_message_time[user_id] < COOLDOWN:
        await message.answer("СПАМИТЬ ЗАПРЕЩЕНО! БАН 30 СЕК.")
        return

    last_message_time[user_id] = now

    if message.text:
        text = message.text.strip()
        banned_words = ['http', 'реклама', 'подпишись']
        if any(word in text.lower() for word in banned_words) or len(text) < 10:
            await message.answer("Что за хуйню ты мне шлешь??")
            return
        await bot.send_message(CHANNEL_ID, f"Крысиный писк:\n{text}")
        await message.answer("Отправлено!")

    elif message.photo:
        caption = message.caption or ""
        await bot.send_photo(CHANNEL_ID, message.photo[-1].file_id, caption=f"🐀 Анонимное фото:\n{caption}")
        await message.answer("Спасибо за мем.")

    elif message.video:
        caption = message.caption or ""
        await bot.send_video(CHANNEL_ID, message.video.file_id, caption=f"🐀 Анонимное видео:\n{caption}")
        await message.answer("Видеопруф зафиксирован.")

    else:
        await message.answer("Пока что я принимаю только текст, фото и видео. А говно которое ты прислал, я не пон.")
