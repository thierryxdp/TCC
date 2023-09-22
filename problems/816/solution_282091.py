def maiores(lista,n):
    '''funcao que recebe uma lista de numeros inteiros e um inteiro n e retorna outra lista contendo os numeros da lista original que sao maiores do que n ordenados dem ordem crescente 
list, int -> list'''
    lista_saida=[]
    lista2=lista+[n]
    x=list.index(lista2,n)
    for i in lista2:
        if i>lista2[x]:
            lista_saida=lista_saida+[i]
            list.sort(lista_saida)
            return lista_saida