def filtraMultiplos(lista_n,n):
    '''Funcao que recebe uma lista de numeros e um numero n como entrada e retorna outra lista contendo apenas os 
    elementos da lista original divisiveis por n;
    list,int->list'''
    
    numeros=[]
    indice=0
    
    while indice<len(lista_n):
        if (lista_n[indice])%n==0:
            numeros=list.append(numeros,lista_n[indice])
            indice=indice+1
            return numeros