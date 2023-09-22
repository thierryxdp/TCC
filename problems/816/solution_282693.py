def maiores(lista_numero,n):
    '''Uma função dada uma lista de numeros inteiros e um numero inteiro n,
       e retorna outra lista, que contenha todos os numeros da lista original 
       maiores que n ordenados em ordem crescente. list[int],int -> list[int]'''
    numero = lista_numero
    list.sort(lista_numero)
    if lista_numero(0) < n:
    return lista_numero.pop(0)