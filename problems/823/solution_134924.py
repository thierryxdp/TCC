def faltante(lista):
    """ """
    ct = 0
    lista1 = sorted(range(1, len(lista)+1))
    
     
    while ct < len(lista)+1:
        ct = ct + 1 
        if lista[ct] == lista1[ct] and ct == len(lista)-1:
            return lista[ct]     
            
        if lista[ct] != lista1[ct]:
            return lista1[-1]+1