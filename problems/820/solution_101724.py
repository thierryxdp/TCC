def posLetra(texto,letra,n):
    """retorna a posicao da letra na ocorrencia n na string;
    str,str,int -> int"""
    i=0
    cnt=0
    
    if str.count(texto,letra)<n:
        return -1
    
    while i<len(texto) and cnt<n:
        if texto[i]==letra:
            cnt=cnt+1
        i=i+1
            
    return str.index(texto,texto[i])