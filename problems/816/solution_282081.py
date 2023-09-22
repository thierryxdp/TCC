def maiores(lista,n):
    '''funcao que recebe uma lista de numeros inteiros e um inteiro n e retorna outra lista contendo os numeros da lista original que sao maiores do que n ordenados dem ordem crescente 
list, int -> list'''
    lista_maiores=[]
    for numero in lista:
        if numero>n:
            list.extend(lista_maiores,[numero])
            list.sort(lista_maiores)
            return lista_maiores
        else:
            return []