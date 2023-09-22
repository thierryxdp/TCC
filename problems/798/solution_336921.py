def freq_palavras(frases):
    """dada uma frase de entrada, retorna um dicionário
    onde cada palavra dessa frase é uma chave e tem como
    valor o número de vezes que ela aparece
    str-->dict"""
    dicionario={}
    frases=frases.strip()
    frases=frases.split('')
    for palavra in frases:
        if palavra in dicionario:
            dicionario[palavra]=dicionario[palavra]+1
        else:
            dicionario[palavra]=1
    return dicionario