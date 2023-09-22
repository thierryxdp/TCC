def filtraMultiplos(lista,n):
    '''retorna todos os números da lsita que forem múltiplos de n
    lista,int->lista'''
    multi=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            multi.append(lista[i])
        i+=1
    return multi