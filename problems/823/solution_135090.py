def faltante(lista):
    """Função que dados uma lista retorne o número faltante.
    list-> int"""
    ct = 0
    lista1 = range(1, len(lista)+1)
    lista2 = sorted(lista1)
    
     
    while ct < len(lista):
        lista3 = lista2[-1]
        ct = ct + 1 
        
        if lista[0] != lista1[0]:
            return lista3
        
        if lista[ct] == lista1[ct] + 1 and ct == len(lista)-1:
            return lista1[ct-1] 
            
        if lista[ct] == lista1[ct] and ct == len(lista)-1:
            return lista2[ct]+1
            
        if lista[0] != lista1[0]:
            return lista2[ct-1]
        
        if lista[ct] != lista1[ct]:
            return ct+1
            
       
    return lista3