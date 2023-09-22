# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras ( frases ) :
    ''' Mostra um dicionário contendo quantas vezes cada palavra aparece na frase'''
    dicionario = {}
    frases = frases.split ( )
    c1 = 0
    while ( c1 < len ( frases ) ) :
        if ( frases [ c1 ] in dicionario.keys ( ) ) :
            dicionario [ frases [ c1 ] ] += 1
        if ( frases [ c1 ] not in dicionario.keys ( ) ) :
            dicionario [ frases [ c1 ] ] = 1    
        c1 += 1
    return dicionario