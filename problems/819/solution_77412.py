def filtraMultiplos(lista,n):
    """ faz a filtragem de uma lista de números que são múltiplos de um
    números n; list,int->list"""
    
    lista1=[]
    indice=0
    while(indice<len(lista)):
        if(lista[indice]%n==0):
            lista1+=(lista[indice],)
        indice+=1 
    return lista1