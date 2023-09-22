def soma_h(numero):
    lista = []
    for x in list(range(1,numero+1)):
        adicionar = (x**-1)+((x+1)**-1)
        lista.append(adicionar)
    return sum(lista)