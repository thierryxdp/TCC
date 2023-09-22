def fatorial(numero):
    proximo=0
    lista=list(range(numero+1))
    lista2=list.copy(lista[1:])
    while proximo<len(lista2):
        proximo=proximo+1
        valor=lista2[proximo]*lista2[proximo+1]
    return valor