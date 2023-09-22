# int, int, int, int -> 
def filtra_pares(tupla):
    lista_tupla = []
    for contador in tupla:
        if contador%2==0:
            lista_tupla.append(contador)
    return tuple(lista_tupla)