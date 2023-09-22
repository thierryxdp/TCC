def hashtag(s):
    '''retorna a string dada com o caractere "#" no início, no meio e no final:
    str --> str'''
    frase = s
    q = len(frase)
    final = '#'+frase[0:q//2]+'#'+frase[q//2:q]
    return final