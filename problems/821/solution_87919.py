def fatorial(n):
    """Funcao que calcula o fatorial de um numero; int -> int"""
    
    fatorial = 0
    listafat = list(range(n,0,-1))
    i = 0
   
    if n == 1:
        return n
            
    while len(listafat) > 1:
        
        if i<len(listafat):
            fatorial = listafat[i]*listafat[i+1]
            del listafat[i]
            del listafat[i]
            list.insert(listafat,0,fatorial)
        
    return fatorial