def posLetra (frase,letra,num):
    """retorna em que posição da string a ocorrência da letra 
    está"""
    n = 0
    posicao = []
    
    while n < str.count(frase,letra):
        if frase[n] in letra: 
            list.append(posicao,n)
            n = n + 1
        else:
            return -1
        
    return lista[n-1]