def fatorial(numero):
    lista = list(range(1,numero+1))
    i = 0
    while i<numero:
        lista[i+1] = lista[i+1]*lista[i+2] 
    i = i + 1
    return lista[numero]