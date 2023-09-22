def maiores(lista,n):
    '''funcao que recebe uma lista de numeros inteiros e um inteiro n e retorna outra lista contendo os numeros da lista original que sao maiores do que n ordenados dem ordem crescente 
list, int -> list'''
    for i in lista[0:]:
        if i>n:
            lista_maiores=list(i)
            list.sort(lista_maiores)
            return lista_maiores