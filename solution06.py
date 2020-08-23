sport = int(input("Введите количество километров которые вы пробежали в первый день >>>"))
desired = int(input("Введите желаемый результат количество километров, которые Вы хотели бы достичь >>>"))

days = 1

while sport <= desired:

     days = days + 1
     sport = (sport + (sport * 0.1))




else:
     print("Готово!")
     print("Желаемй результат в {} километров, можно достичь на {} день!".format(round(sport),days))
