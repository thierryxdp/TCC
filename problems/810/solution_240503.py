def inverte (frase):
    palavras=frase.split( )
    pontuacao=re.sub('.,')
    palavras.reverse( )
    return ' '.join(palavras)