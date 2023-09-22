def fatorial(numero):
    """função que calcula a fatorial de um numero e retorna o valor da fatoração desse numero"""
    total=numero
    while numero!=0:
        if numero>1:
                total=total*(numero-1)
                numero-=1
        else:
                numero-=1
    return total