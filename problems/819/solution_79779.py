def filtraMultiplos(lista,n):
    '''
Função que dada uma lista retorna os números que são 
divisiveis por n.
list,int-->list
    '''
    listaN=[]
    indice=0

    while indice<len(lista):
        if lista[indice]%n==0:
            list.append(listaN,lista[indice])
        
        indice=indice+1
    return listaN