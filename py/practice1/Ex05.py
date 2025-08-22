def sum(number1, number2):
  return number1 + number2


def substract(number1, number2):
  return number1 - number2


def multiple(number1, number2):
  return number1 * number2


def divide(number1, number2):
  return number1 / number2


number1 = 10
number2 = 5

print(f"足し算：{number1} + {number2} = {sum(10, 5)}")
print(f"引き算：{number1} - {number2} = {substract(10, 5)}")
print(f"掛け算：{number1} × {number2} = {multiple(10, 5)}")
print(f"割り算：{number1} ÷ {number2} = {divide(10, 5)}")