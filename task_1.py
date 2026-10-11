from queue import Queue
import random
import time


request_queue = Queue()


def generate_request():
    request_id = random.randint(1000, 9999)
    request_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    request = f"Заявка №{request_id} від {request_date}"

    request_queue.put(request)
    print(f"Створено: {request}")


def process_request():
   while not request_queue.empty():
        request = request_queue.get()
        print(f"Обробляється: {request}")
        time.sleep(2)
        print(f"{request} оброблена")



while True:
    # Генеруємо від 1 до 10 нових заявок
    for _ in range(random.randint(1, 10)):
        generate_request()

    # Обробляємо одну заявку
    process_request()

    # Показуємо кількість заявок у черзі
    print(f"Заявок у черзі: {request_queue.qsize()}")

    command = input("Натисніть Enter для продовження або 'q' для виходу: ")

    if command.lower() == "q":
        break