def maiores(lista,n):
    '''funcao que recebe uma lista de numeros inteiros e um inteiro n e retorna outra lista contendo os numeros da lista original que sao maiores do que n ordenados dem ordem crescente 
list, int -> list'''
    for numero in lista:
        if numero<int(n):
            lista=list.remove(lista,numero)
            return lista