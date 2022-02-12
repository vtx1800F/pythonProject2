s=0
ticket=int(input('Введите кол-во билетов\n'))
for i in range(1,ticket+1):
    age=int(input(f'Введите возраст для билета № {i}\t'))
    if 18>age:
        price=0
        s += price
        print("цена билета 0")
    elif 18<= age<=25:
        price=990
        s += price
        print("цена билета 990")
    else:
        price=1390
        s += price
        print("цена билета 1390")
    print("сумма к оплате",s)
if ticket> 3:
    s=s-(s*0.1)
    print (s)