def soma_h(numero):
    lista = []
    for x in list(range(2,numero+1)):
        adicionar = round((x**-1)+((x+1)**-1),2)
        lista.append(adicionar)
    return lista