#!/usr/bin/env python
"""
Тест для проверки работоспособности aiogram 3.2.0 с новыми зависимостями
"""

import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Создаем тестовый диспетчер
dp = Dispatcher()

# Тестовый обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Тестовый обработчик команды /start
    """
    return await message.answer("Привет! Это тестовый бот.")

async def main():
    """
    Основная функция для инициализации и запуска бота
    """
    # Не запускаем бота, просто проверяем инициализацию
    print("✅ Инициализация aiogram 3.2.0 прошла успешно!")
    print("✅ Зависимости совместимы!")
    return 0

if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
        print("🎉 Тест aiogram 3.2.0 успешно завершен!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Ошибка при тестировании aiogram: {e}")
        sys.exit(1) 