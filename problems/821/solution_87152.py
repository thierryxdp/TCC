def fatorial(num):
    "Retorna o fatorial de um numero, dado: o numero(num)"
    c= cont=1
    while cont<num:
        cont += 1
        c*=cont
    return c