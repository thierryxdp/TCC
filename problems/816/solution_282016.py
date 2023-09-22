def maiores(lista,n):
    '''funcao que recebe uma lista de numeros inteiros e um inteiro n e retorna outra lista contendo os numeros da lista original que sao maiores do que n
    list, int -> list'''
    lista_maiores=[]
    for numero in lista:
        if numero>n:
            list.append(lista_maiores,numero)
            return lista_maiores