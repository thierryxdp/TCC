def posLetra(frase,letra,n):
    '''retorna em que posição da string a ocorrencia da letra está'''
    '''str,str,int -> int'''
    
    pos = 0 
    rep = 0
    
    while pos < len(frase):
       
       if frase[pos] == letra:
            rep = rep + 1
        
            if rep == n:
                return pos
    pos = pos + 1
        
    return -1