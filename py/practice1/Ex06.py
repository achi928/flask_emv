def divide_numbers(a, b):
  if b == 0:
    raise ZeroDivisionError("0で割ることはできません")
  result = a / b
  return result

num1 = 10
num2 = 0
try:
  print(divide_numbers(num1, num2))
except ZeroDivisionError as e:
  print(f"{e}")
  
  
def divide(num1, num2):
  try:
    result = num1 / num2
    print(result)
  except ZeroDivisionError:
    print("0で割ることはできません")
    
divide(num1, num2)