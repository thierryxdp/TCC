def insere(lista_numero,n):
    '''retorna uma lista com numeros maiores que n da lista original'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    lista_numero=[n::-1]
    list.remove(lista_numero,n)
    return lista_numero