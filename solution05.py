
while 1:
    revenue = input("Введите сумму выручки компании  >>>")
    try:
        revenue = float(revenue)
        break
    except ValueError:
        print('Не является числом')

while 2:

   costs = input("Введите сумму издержек компании  >>>")

   try:
     costs = float(costs)
     break
   except  ValueError:
    print('Не является  числом')


a = revenue - costs
c = int((a / revenue) * 100)



if   revenue > costs:
        print("Компания работает в прибыль — выручка больше издержек.")
        print("Рентабельность продаж компании состовляет {}% !".format(c))
        while 3:
            Employee = input("Введите численность сотрудников компании  >>>")
            try:
                Employee = float(Employee)
                break
            except ValueError:
                print('Не является числом')
        print("Прибыль компании в расчете на одного сотрудника состовляет {} !", (a // Employee ))

if   revenue < costs:
        print("Компания работает в убыток — издержки больше выручки.")

elif revenue == costs:
            print("Компания работает в 0!!!")









