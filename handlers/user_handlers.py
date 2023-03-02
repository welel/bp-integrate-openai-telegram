from aiogram import F, Router
from aiogram.types import Message


router: Router = Router()


@router.message(F.content_type == 'text')
async def process_message(message: Message):
    """Принимает все текстовые сообщения."""
    await message.answer(text="echo")
