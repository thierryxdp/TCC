def uppCons(frase):
    """Este código recebe uma frase, e coloca em maiuscula
    todas as consoantes da frase, na mesma ordem em que se 
    encontravam.
    Recebe: str
    Retorna: str"""
    posicao = 0
    resposta = ''
    
    while posicao < len(frase):
        if frase[posicao] in 'bcdfghjklmnpqrstvwxyz':
            resposta = resposta + str.upper(frase[posicao])
        else:
            resposta = resposta + frase[posicao]
        posicao = posicao + 1
    return resposta