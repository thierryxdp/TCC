def faltante(L):
    """funcao que retorna o numero da peca que falta"""
    i=0
    L= list.sort(L)
    
    while i< len(L):
        if L[i]-1==L[i-1]:
            i = i+1
            
    return i