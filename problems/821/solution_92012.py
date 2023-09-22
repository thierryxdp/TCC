def fatorial(numero):
    douglar=1
    contador=1
    outro=numero
    while contador<outro:
        douglar*=numero
        numero-=1
        contador+=1
    return douglar