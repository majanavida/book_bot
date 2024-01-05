import asyncio
import logging 
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_main_menu


# Инициализируем логгер 
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота 
async def main():
    # Конфигурация логгирования 
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    
    # Выводим информацию о запуске бота 
    logger.info('Bot started successfully')
    
    # Загружаем конфиг в переменную конфиг 
    config: Config = load_config()
    
    # Инициализируем бот и диспетчер 
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()
    
    # Настройка главного меню бота 
    await set_main_menu(bot)
    
    # Регистрация роутеров в диспечтере 
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    
    # Пропуск накопившихся апдейтов и запуск polling 
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    asyncio.run(main())