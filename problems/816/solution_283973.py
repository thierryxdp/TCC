def maiores(lista_numero,n):
    '''dada uma lista e um inteiro n, retorna uma lista com todos os elementos maiores que n na lista original
    list,int-->list'''
    if n not in lista_numeros:
        list.append(lista_numeros,n)
    list.sort(lista_numeros)
    lista_final=lista_numeros[list.index(lista_numeros,n) + 1:]
    return lista_final