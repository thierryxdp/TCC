def filtraMultiplos(lista,n):
    '''Função que retorna todos os números da lista
    divisiveis pelo numero n
    entrada= list,int
    saida=list'''
    f=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            f= f+[lista[i]]
        i=i+1
    return f