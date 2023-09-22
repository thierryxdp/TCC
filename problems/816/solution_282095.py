def maiores(lista,n):
    '''funcao que recebe uma lista de numeros inteiros e um inteiro n e retorna outra lista contendo os numeros da lista original que sao maiores do que n ordenados dem ordem crescente 
list, int -> list'''
    lista_saida=[]
    list.sort(lista)
    list.append(lista,n)
    x=list.index(lista,n)
    if lista[0:x]>lista[x]:
        return lista_saida