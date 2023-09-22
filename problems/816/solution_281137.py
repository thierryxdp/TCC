def maiores(lista_numero, n):
    '''Retorna uma lista com todos os números da lista original maiores que n
list, int -> list'''
    lista_numero=insere(lista_numero, n)
    primeiromaior=list.index(lista_numero,n)+1
    return lista_numero[primeiromaior:]