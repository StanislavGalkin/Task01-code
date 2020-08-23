Max_number = int(input("Введите положительное число  >>>"))

ls = []
while Max_number > 10:
    ls.append( Max_number % 10)
    Max_number //= 10
r = max(ls)
print("Самая большая цифра в этом числе: {} ".format(r))
