def inverte(frase):
    '''Esta funçao inverte a posiçao das palvras na frase
    string ==> string '''
    palavras = str.split(frase, ' ')
    palavras = palavras.reverse()
    palavras = str.join(' ', palavras)
    
    return (palavras)