def maiores(lista,n):
    '''funcao que recebe uma lista de numeros inteiros e um inteiro n e retorna outra lista contendo os numeros da lista original que sao maiores do que n ordenados dem ordem crescente 
list, int -> list'''
    list.append(lista,n)
    list.sort(lista)
    i=list.index(lista,n)
    return lista[i+1:]