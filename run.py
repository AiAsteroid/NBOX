#!/usr/bin/env python3

import sys
import traceback
from facefusion import core
import logging
import os

log_dir = '../LOGS'
if not os.path.exists(log_dir):
	os.makedirs(log_dir)

logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	handlers=[
		logging.FileHandler(os.path.join(log_dir, 'facefusion_error.log'), mode='w'),
		logging.StreamHandler(sys.stdout)
	]
)

logger = logging.getLogger(__name__)


def handle_exception(exc_type, exc_value, exc_traceback):
	if issubclass(exc_type, KeyboardInterrupt):
		sys.excepthook(exc_type, exc_value, exc_traceback)
		return

	logger.critical("Необработанное исключение:", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception

if __name__ == '__main__':
	try:
		logger.info("Запуск приложения...")
		core.cli()
	except Exception as e:
		logger.error("Произошла критическая ошибка:")
		logger.error(str(e))
		logger.error("Полный стек вызовов:")
		logger.error(traceback.format_exc())
		raise
