def freq_palavras(frases):
    """ Função que transforma a frase em um dicionário onde cada palavra é uma chave e tenha como valor o número de vezes que a palavra aparece na frase
    str -> dic """
    dicionario={}
    frase=str.split(frases,' ')
    for palavra in frase:
        if palavra in dicionario:
            dicionario[palavra]+=1
        else:
            dicionario[palavra]=1
    return dicionario