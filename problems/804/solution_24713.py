#Start your python function here
def filtra_pares(elementos):
    lista_pares = ["","","",""]
    if elementos[0]%2 == 0:
        lista_pares[0] = elementos[0]
    elif elementos[1]%2 == 0:
        lista_pares[1] = elementos[1]
    elif elementos[2]%2 == 0:
        lista_pares[2] = elementos[2]
    elif elementos[3]%2 == 0:
        lista_pares[3] = elementos[3]
    tuple_pares = (lista_pares)
    return tuple_pares