def posLetra (frase,letra,num):
    """retorna em que posição da string a ocorrência da letra 
    está"""
    n = 0
    posicao = []
    
    if num <= str.count(frase,letra):
        while n < len(frase):
            if frase[n] in letra:
                list.append(posicao,n)
            n = n + 1 
        return posicao[num-1]
    else:
        return - 1