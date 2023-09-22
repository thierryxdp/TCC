def qtd_divisores(x:int)->int:
    "Contando os divisores de um número."
    i = 0
    for i in range(1,x+1):
        if x % i == 0:
            i += 1
    return i