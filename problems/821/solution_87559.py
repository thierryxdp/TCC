def fatorial(numero):
    lista= list(range(1,numero+1))
    i = 0 
    total = 1
    while i < len(lista):
        total = total * lista[i]
        i = i + 1
    return total