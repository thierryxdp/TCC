def conta_frases(texto):
    '''retorna o número de frases, separadas por ponto final;
    ponto de exclamação, ponto de interrogação e reticências
    str -> int'''
    frase_nova1=str.replace(texto,'!','.')
    frase_nova2=str.replace(frase_nova1,'?','.')
    frase_nova3=str.replace(frase_nova2,'...','.')
    frase4=str.split(frase_nova3,'.')
    frases=len(frase4)
    frases=frases-1
    return frases