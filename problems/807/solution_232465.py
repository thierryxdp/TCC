def conta_frases(frase):
    ''' função que conta os numeros de frases'''
    ponto=frase.replace('!','.')
    ponto2=ponto.replace('?','.')
    ponto3=ponto2.replace('...','.')
    ponto4=ponto3.rsplit('.')
    frases=ponto4.split('.')
     return len(frases)