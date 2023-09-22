def carros_passageiros(p):
    return p // 4

def carros_motoristas(m):
    return m // 1

def carros(a, b):
    a = carros_passageiros(p)
    b = carros_motoristas(m)
    return (a + b)//2