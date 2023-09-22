def filtraMultiplos(lista,n):
    '''função que retorna os multiplos de um numero n'''
    i=0
    resultado=[]
    while i<len(lista):
        if lista[i]%n==0:
            list.append(resultado,lista[i])
        i=i+1
    return resultado