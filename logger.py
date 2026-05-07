import logging
import os
from datetime import datetime


def setup_logger(name: str) -> logging.Logger:
    """Настройка логгера для приложения"""

    os.makedirs('logs', exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Формат: время - уровень - сообщение
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Лог в файл
    file_handler = logging.FileHandler('logs/app.log')
    file_handler.setFormatter(formatter)

    # Лог в консоль
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
