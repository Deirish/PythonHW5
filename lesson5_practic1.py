string = "Hello world, Hello world".split()
def lower_reg(string):
    return string.lower()
def upper_reg(string):
    return string.upper()
print(list(map(lower_reg, string)))
print(list(map(upper_reg, string)))