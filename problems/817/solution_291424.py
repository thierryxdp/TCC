def maiores(lista,n):
    
    lista.append(n)
    lista.sort()
    posicao= lista.index(n)
    
   
    return lista[posicao +1::]

def acima_da_media(lista):
    """ """
    
    n= sum(lista)//len(lista) +1 
    
   
    return maiores(lista,n)