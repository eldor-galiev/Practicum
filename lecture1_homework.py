print("Введите стороны треугольника")
a = int(input())
b = int(input())
c = int(input())
answer = "треугольник "
if (a+b)>=c and (a+c) >= b and (b+c) >= a:
    if a == b or a == c or b == c:
        if a==b and b==c:
            answer += "равносторонний"
        else:
            answer += "равнобедренный"
            if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (c ** 2 + b ** 2 == a ** 2):
                answer += " и прямоугольный"
    else:
        if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (c**2 + b**2 == a**2):
            answer += "прямоугольный"
        else:
            answer += "обычный"

else:
    answer += " не существует"
print(answer)