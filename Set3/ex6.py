OPERATORI_GLOBALI={
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b
}

def apply_operator(operator,a,b):
    if operator in OPERATORI_GLOBALI:
        return OPERATORI_GLOBALI[operator](a,b)
    else:
        return None

print(apply_operator("+",2,3))
print(apply_operator("*",2,3))
print(apply_operator("/",2,3))
print(apply_operator("%",2,3))