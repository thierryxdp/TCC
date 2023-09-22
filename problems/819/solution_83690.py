def filtraMultiplos(l,n):
    '''Funcao que recebe uma lista de numeros e um numero n como entrada e retorna outra lista contendo apenas os 
    elementos da lista original divisiveis por n;
    list,int->list'''
    
    numeros=[]
    indice=0
    
    while indice<len(l):
        if ((l[indice])%n) == 0:
            list.append(numeros,l[indice])
        indice=indice+1
    return numeros