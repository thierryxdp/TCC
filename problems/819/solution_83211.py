def filtraMultiplos(lista_numero, n):
    '''Função que deve retornar uma lista contendo todos os elementos da lista original, list, str -> list'''
    i = 0
    listanum = list.append(lista_numero, n)
    while i<len(lista_numero):
        if [i]%lista_numero:
            listanum = i
        i = i + 1
    return listanum