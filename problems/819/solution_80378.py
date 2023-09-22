def filtraMultiplos(lista,n):
    '''Uma função que filtra os multiplos de n que é recebido com a lista
    e retorna uma lista lis,int->list'''
    i=0
    lista_final = []
    while i<len(lista):
        if lista[i]%n == 0:
                   lista_final.append[i]
        i=i+1
    return lista_final