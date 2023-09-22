def fatorial(num):
    i = 0
    mult = 1
    lista = list(range(1,num+1))
    while i < len(lista):
        mult = mult * lista[i]
        i = i + 1
    return mult