class Create:
    counter = 0 #статична змінна класа - належить ВСІМ
    #екземплярам класа! Також до неї можна звернутися
    # на пряму , не створюючи жодного екземпляра класа

    def __init__(self):#під час створення екземплярів класа
        Create.counter += 1#лічільник змінюється на +1
    @staticmethod #Статичний метод, якій теж належить всьому класу
    #і ми можемо звернутися до нього без екземплярів класа
    def Show():
        print("Counter = ",Create.counter)

#створили 3 екземпляра класа
first = Create()
second = Create()
third = Create()
four = Create()
#виводимо на екран лічільник
print("Counter = ",Create.counter)
Create.Show()