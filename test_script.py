import logging
import time

from multiprocessing import Process
from threading import Thread

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

SLEEP_TIME_CONST = 10
NUMBER_OF_RUNNERS = 3

def test_runner(index, sleep_time):
    """Тестовый раннер"""
    while True:
        logger.debug(f"Runner working {index}")
        time.sleep(sleep_time)

def multiprocessing_run(n):
    """Запуск через multiprocessing"""
    for i in range(n):
        p = Process(target=test_runner, args=(i, SLEEP_TIME_CONST))
        p.start()

def threading_run(n):
    """Запуск через threading"""
    for i in range(n):
        t = Thread(target=test_runner, args=(i, SLEEP_TIME_CONST))
        t.start()


if __name__ == "__main__":
    multiprocessing_run(NUMBER_OF_RUNNERS)