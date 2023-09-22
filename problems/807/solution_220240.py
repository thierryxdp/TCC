def conta_frases(frase):
    '''Cálcula o quantitativo de frases terminadas com 
    pontuação, mas antes transforma todas as pontuações(?,!,...) para 
    ponto final.
    str ->int'''
    f2=frase.replace('?','.')
    f2=f2.replace('!','.')
    f2=f2.replace('...','.')
    return len(f2.strip().split('.'))-1