def fatorial(numero):
    lista = []
    contador = 0
    listanumero = list(range(numero))
    while contador < numero:
        lista = lista + [sum(list(range(listanumero[contador])))]
    	contador = contador + 1
    return lista