def uppCons(frase):
    '''
    Função que recebe uma frase e retorna a frase com todas
    as suas consoantes maiúsculas.
    
    str -> str
    '''
    posicao = 0
    modificada = ''
    while posicao < len(frase):
        if frase[posicao].lower() in 'bcçdfghjklmnpqrstvwxyz':
            modificada = modificada + frase[posicao].upper()
        else:
            modificada = modificada + frase[posicao]
    	posicao = posicao + 1
    return modificada