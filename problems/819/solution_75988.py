#list(int),int->list
def filtraMultiplos(lista,n):
    lista_valida = []
    for elem in lista:
        if elem > 0:
            lista_valida.append(elem)
            return lista_valida