def uppCons(frase):
    '''
    dada uma frase como argumento, a retorna com
    todas as suas consoantes em maisculo
    dados de entrada: str
    retorna:str
    '''
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvwxyz':
            frase = frase[:contador] + str.upper(contador) +
            frase[contador + 1:]
        contador + 1
    return frase