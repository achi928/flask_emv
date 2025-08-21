print((int)(-2.9))

import math

print(math.sqrt(4))

print(math.pi)


def bmi(height, weight) :
    return weight / (height / 100.0) ** 2
  
print(bmi(160, 50))

# def ft_to_cm(f, i) :
#     result = 
#     return i
    
# assert round(ft_to_cm(5, 2) - 157.48, 6) == 0


# 最大公約数と、最大公倍数
def kouyakusu(num1, num2) :
    while num2 != 0:
        r = num1 % num2
        num1 = num2
        num2 = r
    return num1
        
print(kouyakusu(30, 10))


print('干支は', '未', 'です')
print('干支は', '未', 'です', sep=',')

templete = '名前は{}です。年齢は{}です'
text = templete.format('山田', '21')
print(text)