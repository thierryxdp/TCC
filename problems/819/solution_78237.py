def filtraMultiplos(lista , n):
    '''função que filtra os multiplos de uma lista ,  e retorna uma lista com apenas os multiplos de de um certo valor n'''
    lista_valida = []
    for elem in lista:
        if elem % n ==0:
            lista_valida.append(elem)
    return lista_valida