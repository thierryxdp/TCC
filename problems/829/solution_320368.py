def soma_h(numero):
    lista = [0,1]
    for x in list(range(1,numero+1)):
        somar = (lista[x])+(x**-1)
        lista.append(somar)
    return lista