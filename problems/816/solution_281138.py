def insere(lista_numero, n):
    '''Retorna a lista inserida, com o termo n, em ordem crescente
list, int -> list'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

#Questão4
def maiores(lista_numero, n):
    '''Retorna uma lista com todos os números da lista original maiores que n
list, int -> list'''
    lista_numero=insere(lista_numero, n)
    primeiromaior=list.index(lista_numero,n)+1
    return lista_numero[primeiromaior:]