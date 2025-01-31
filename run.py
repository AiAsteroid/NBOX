#!/usr/bin/env python3

import sys
import traceback
from facefusion import core
import logging

# Настраиваем логирование в файл и консоль
logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  handlers=[
    logging.FileHandler('ERROR.log', mode='w', encoding='utf-8'),
    logging.StreamHandler(sys.stdout)
  ]
)

logger = logging.getLogger(__name__)

def handle_exception(exc_type, exc_value, exc_traceback):
  if issubclass(exc_type, KeyboardInterrupt):
    sys.__excepthook__(exc_type, exc_value, exc_traceback)
    return
  logger.critical("Необработанное исключение:", exc_info=(exc_type, exc_value, exc_traceback))

# Устанавливаем перехватчик необработанных исключений
sys.excepthook = handle_exception

if __name__ == '__main__':
  logger.info("Запуск приложения...")
  try:
    core.cli()
  except Exception as e:
    logger.error(f"Критическая ошибка: {str(e)}")
    logger.error("Полный стек вызовов:")
    logger.error(traceback.format_exc())
    sys.exit(1)
