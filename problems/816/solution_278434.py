def maiores(lista,n):
    '''A função recebe uma lista de números inteiros (valores numéricos int) e
    um número inteiro n e retorna outra lista composta por todos os números da
    lista dada maiores que n.
    Parâmetro de entrada: list,int
    Valor de retorno: list'''
    #Ordenando a lista
    list.sort(lista)
    #Indicando a posição de n na lista
    i=list.index(lista,n)
    #Contando quantas vezes n aparece na lista
    vezes=list.count(lista,n)
    #Formando a lista de números maiores que n
    lista_maiores=lista[i+vezes::]
    return lista_maiores