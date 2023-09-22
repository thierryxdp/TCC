def posLetra (frase,letra,num):
    """retorna em que posição da string a ocorrência da letra 
    está"""
    n = 0
    posicao = []
    
    while n <= str.count(frase,letra):
        if frase[n] in letra: 
            posicao = list.append(posicao,n)
            n = n + 1
        elif frase[n] not in letra:
            n+=1 
         

    return posicao[n-1]