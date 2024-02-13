import pyautogui
import time

start_time = time.time()  # сохраняем текущее время

while True:
    x, y = pyautogui.position()
    print(f"Координаты мыши: X={x}, Y={y}")

    elapsed_time = time.time() - start_time  # вычисляем прошедшее время

    if elapsed_time >= 3:
        print("Прошло 10 секунд. Прекращение работы цикла.")
        break

    time.sleep(1)  # добавим небольшую задержку, чтобы не перегружать вывод
