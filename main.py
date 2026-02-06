x = 10
name = "Yaroslav"
is_student = True

if is_student:
    print("Вчиться")
else:
    print("He вчиться")

print(x)
print(name)
print(is_student)
print("Hello, world")

user = "Witcher204"
color = "Red"
is_epstein = True
number = 31

print(user)
print(color)
print(is_epstein)
print(number)

numbe = 5.5
numb = 10

print(number / numb)

first_name = "Ярослав"
last_name = "Котенко"
full_name = first_name + " " + last_name
print(full_name)

imia = input("Введи ім'я та вік: ")
print(imia)

name, agee = input("Введи ім'я та вік: ").split()

while True:
    try:
        age = int(input("Введи вік: "))
        break
    except ValueError:
        print ("Це не число! Спробуйте знову через 5 секунд.")

print("Твій вік:", age)

while True:
    text = input("Введи текст (exit для виходу): ")

    if text == "exit":
        break

print ("Ти написав: ", text)

while True:
     password = input("Пароль: ")
    
     if password == "1234":
        print("Ласкаво просимо в аккаунт!")
        break
     else:
         print("Невірний пароль, спробуйте ще раз пізніше.") 
