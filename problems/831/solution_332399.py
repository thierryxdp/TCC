def lingua_p(palavra):
    '''
    função que recebe como parâmetro uma palavra e retorna
    esta mesma palavra com após cada vogal um "p" seja 
    introduzido 
    str -> str
    '''
    minusculo = str.lower(palavra)
    posicao = 0
    palavra_p = ''
    
    while posicao < len(minusculo):
        if minusculo[posicao] not in "aeiouáéú":
            palavra_p = palavra_p + minusculo[posicao]
        
        else:
            palavra_p = palavra_p + minusculo[posicao] + "p" + minusculo[posicao]
        posicao = posicao + 1
    return palavra_p