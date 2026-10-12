from queue import Queue
import random
import time


request_queue = Queue()
request_id = 0


def generate_request():
    global request_id

    request_id += 1

    request = f"Талон №{request_id} | Дата: {time.strftime('%Y-%m-%d %H:%M:%S')}"

    request_queue.put(request)
    print(f"Видан {request}")


def process_request():
    
    if not request_queue.empty():
        time.sleep(10)
        request = request_queue.get()
        print(f"В процессі, початок сессії в {time.strftime('%H:%M:%S')}: {request}")
        time.sleep(10)
        print(f"{request} сессії завершена в {time.strftime('%H:%M:%S')}")
    else:
        print("Черга порожня")


while True:
    # Генеруємо від 1 до 3 нових заявок
    for _ in range(random.randint(1, 3)):
        generate_request()

    # Обробляємо одну заявку
    process_request()

    # Показуємо кількість заявок у черзі
    print(f"Заявок в черзі: {request_queue.qsize()}")

    command = input("Натисніть Enter для продовження або 'q' для виходу: ")

    if command.lower() == "q":
        break