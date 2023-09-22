def insere(lista_numero,n):
    '''recebe e retorna uma lista ordenada crescente com o numero n
    list,int -> list'''
    
    listaA = lista_numero
    listaB = [n]
    listaAB = listaA + listaB
    
    return list.sort(listaAB)