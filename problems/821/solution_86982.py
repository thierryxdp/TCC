def fatorial(numero):
    lista = list(range(1,numero[0]+1))
    i = 0
    while i<numero[0]:
        lista[i] = lista[i]*lista[i+1] 
    i = i + 1
    return lista[numero[0]]