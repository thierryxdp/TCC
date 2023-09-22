def filtraMultiplos(listanumeros, n):
    '''funcao que recebe uma lista de numeros e um numero e retorna uma nova lista contendo todos os elementos da lista original que forem divisivei por n;
     list, int-> list'''
    novalista=[]
    i=0
    while i<len(listanumeros):
        if listanumeros[i]%n:
            novalista= novalista+[listanumeros[i]]
        i=i+1
        
    return novalista