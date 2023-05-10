import numpy as np
import matplotlib.pyplot as plt

with open("settings.txt") as settings:
    temp = [float(i) for i in settings.read().split("\n")]
    print(temp)
data_array = np.loadtxt("data.txt", dtype=int)
#print(data_array)

meas_time = temp[0]*1000
volt = temp[1]
print(meas_time)
print(volt)

data_volt = [i*volt for i in data_array]
#print(data_volt)

point_num  = len(data_array)
time = np.linspace(0, meas_time, point_num)
#print(point_num)

#определяем время зарядки, общее и разрядки
max_value = np.max(data_array)
index_max_value = np.where (data_array== max_value)[0][0]
print(index_max_value)
time_on = time[index_max_value]
total_time = time[len(time)-1]
time_off = total_time - time_on
print(time_on, time_off)

#работа с графиком

plt.figure(figsize=(17, 10))

plt.title("График зависимости U от t") # заголовок
plt.xlabel("t, c") # ось абсцисс
plt.ylabel("U, v") # ось ординат
plt.plot(time, data_volt, color='black', marker='o', linestyle='-', linewidth=1, markersize=6, markevery =20)
plt.minorticks_on()
plt.grid( which = 'major', color='black', linestyle='-', linewidth=1)      # включение отображение сетки
plt.grid( which = 'minor', color='gray', linestyle=':', linewidth=1)      # включение отображение сетки
plt.text(10, 2.5, r'$Время \; зарядки \; \approx 5.72 \; c $', fontsize =18)
plt.text(10, 2.3, r'$Время \; разрядки \; \approx 7.68 \; c $', fontsize =18)
#plt.show()
plt.savefig('graph.png')