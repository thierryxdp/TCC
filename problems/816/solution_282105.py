def maiores(lista,n):
    '''funcao que recebe uma lista de numeros inteiros e um inteiro n e retorna outra lista contendo os numeros da lista original que sao maiores do que n ordenados dem ordem crescente 
list, int -> list'''
    list.sort(lista)
    lista2=lista+[n]
    indice_n=list.index(lista2,n)
    list.sort(lista2)
    return lista2[indice_n+i:]