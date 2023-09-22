def freq_palavras(frase):
    '''Dada um string retorna um dicionário onde cada palavra 
    dessa string é uma chave que tem como valor o número de vezes
    que a palavra aparece.
    str -> dict'''
    
    dici = {}
    frase_list = str.split(frase,' ')
    for palavra in frase_list:
        if palavra not in dici:
            dici[palavra] = 1
        else:
            dici[palavra] = dici[palavra]+1
    return: dici