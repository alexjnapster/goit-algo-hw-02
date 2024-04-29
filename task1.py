import queue
import uuid
import time


def generate_request(q):
    request_id = str(uuid.uuid4())
    q.put(request_id)
    print(f"Згенеровано заявку з ID: {request_id}")


def process_request(q):
    if not q.empty():
        request_id = q.get()
        print(f"Обробляється заявка з ID: {request_id}")
    else:
        print("Немає заявок для обробки.")


def user_interface():
    q = queue.Queue()
    while True:
        print("\n1. Згенерувати нову заявку")
        print("2. Обробити заявку")
        print("3. Вийти з програми")
        choice = input("Введіть ваш вибір (1-3): ")

        if choice == '1':
            generate_request(q)
        elif choice == '2':
            process_request(q)
        elif choice == '3':
            print("Завершення програми.")
            break
        else:
            print("Некоректний вибір, будь ласка, введіть 1, 2, або 3.")


user_interface()
