def inverte (frase):
    palavras=frase.split( )
    palavras.reverse( )
    pontuacao=frase.replace('.',',')
    return ' '.join(palavras)