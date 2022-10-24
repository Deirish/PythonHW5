# Написать функцию которая будет простое число возводить в квардрат.
# Необходимо возвести в квадрат все простые числа в списке используя функцию map

def my_int(x):
    return x*x
l = range(1, 10)
def is_simple(x):
    r = range(2, x)
    for i in r:
     if not x % i:
      return False
    return True
print(list(map(my_int, filter(is_simple,l))))