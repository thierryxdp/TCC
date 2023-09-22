def inverte (frase):
    palavras=frase.split( )
    palavras.reverse( )
    pontuacao=frase.replace('.',',')
    pontuacao.reverse( )
    return ' '.join(palavras)