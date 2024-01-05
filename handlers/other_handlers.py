from aiogram import Router
from aiogram.types import Message

router = Router()

# Этот хендлер будет реагировать на любые действия пользователя, 
# не предусмотренные логикой бота  
@router.message()
async def send_echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)