import sys
import traceback
from facefusion import core
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

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
