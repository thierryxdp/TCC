def carros_passageiros(p):
    return p // 4

def carros_motoristas(m):
    return m // 1

def carros(m, p):
    p = carros_passageiros(p)
    m = carros_motoristas(m)
    return (m + p)//2