def filtraMultiplos(lista,n):
    '''Uma função que filtra os multiplos de n que é recebido com a lista
    e retorna uma lista lis,int->list'''
    i=0
    listafinal = []
    while i<len(lista):
        if lista[i]%n == 0:
              listafinal.append[i]
        i=i+1
    return listafinal