def faltante(lista):
    """Essa função retorna o numero inteiro referente a
    peça que está faltando, dado uma lista.
    lista->int"""
    
    i=0
    lista = list.sort(lista)
    
    p1=0
    p2=0
    
    while i < len(lista):
        
        p1=lista[i]
        p2=lista[i-1]
        
        if (p2+1) != p1:
            return i+1
        i+=1
    return len(lista)