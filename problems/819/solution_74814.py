def divisiveis(lista,n):
    '''função que dada uma lista de números, retorna outra lista contendo somente os múltiplos de n; (list,int)->list'''
    indice=0
    divisiveis=[]

    while indice<len(lista):
        if lista[indice]%n==0:
            divisiveis=divisiveis+[lista[indice],]
            
        indice=indice+1
        
    return divisiveis