def fatorial(numero):
    douglar=1
    contador=1
    while contador<numero:
        douglar*=numero
        numero-=1
        contador+=1
    return douglar