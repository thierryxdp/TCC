def uppCons(frase):
    '''Essa função tem como objetivo mudar as consoantes para letras
    maiúsculas, e deixando as vogais como estão no texto'''
    '''str -> str'''
    P=0
    frase_final=''
    while P<len(frase):
        if frase[P] not in 'ãáaeéiíoóôõuú':
            frase_final= frase_final+ str.upper(frase[P])
            P+= 1
        else:
            frase_final= frase_final+ frase[P]
            P+= 1
    return frase_final