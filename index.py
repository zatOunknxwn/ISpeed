import irsdk
import time

# Создаем объект iRacing SDK
ir = irsdk.IRSDK()

# Ждем пока игра не запустится
while not ir.startup():
    print("Ждем запуска iRacing...")
    time.sleep(1)

print("iRacing запущен!")

try:
    while True:
        # Обновляем данные
        ir.freeze_var_buffer_latest()

        # Данные о твоей машине
        speed = ir['Speed']  # скорость м/с
        lap = ir['Lap']      # текущий круг
        track_pos = ir['TrackPosition']  # положение на трассе в процентах

        print(f"Скорость: {speed:.1f} м/с | Круг: {lap} | Позиция на трассе: {track_pos:.2f}%")

        # Данные о других игроках
        num_cars = ir['NumCars']
        print("Игроки на трассе:")
        for i in range(num_cars):
            car_id = i
            car_speed = ir['CarIdxSpeed'][i]
            car_track = ir['CarIdxTrackPosition'][i]
            print(f"  Игрок {i}: Скорость {car_speed:.1f} м/с, Позиция {car_track:.2f}%")

        print("-" * 50)
        time.sleep(0.5)  # обновляем 2 раза в секунду

except KeyboardInterrupt:
    print("Выход из программы")
finally:
    ir.shutdown()
