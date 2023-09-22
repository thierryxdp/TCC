def maiores(lista,n):
    '''funcao que recebe uma lista de numeros inteiros e um inteiro n e retorna outra lista contendo os numeros da lista original que sao maiores do que n ordenados dem ordem crescente 
list, int -> list'''
    lista_saida=[]
    list.sort(lista)
    lista2=lista+[n]
    x=list.index(lista2,n)
    if lista2[0:x]>lista[x+1]:
        return lista_saida