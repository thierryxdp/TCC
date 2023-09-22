def filtraMultiplos(lista,n):
    '''funçao que recebe uma lista de numeros e um numero como
    entrada e retorna outra lista com os elementos da lista original
    divididos por n'''
    lista2=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            lista2+=[lista[i],]
        i=i+1
    return lista2