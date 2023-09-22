def posLetra (frase,letra,vezes):
    """retorna em que posição da string a ocorrência "vezes" da letra está"""
    
    n = 0 
    posicao = -1 
    
    while n < len(frase):
        if str.count(frase,letra) != posicao:
            posicao = posicao + 1
            n = n + 1
    return posicao