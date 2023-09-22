def soma_h(valor):
    soma=0
    for numero in list(range(valor+1)):
        if numero!=0:
            x=1/numero
            soma= x+soma
    return round(soma,2)
soma_h(10)