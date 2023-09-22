def freq_palavras(frases):
    """dado uma string, retorna um dicionario onde cada palavra
    dessa string seja uma chave e tenha como valor o numero de vezes 
    que a palavra aparece.
    str --> dict"""
    dicionario={}
    frases=frases.strip()
    frases=frases.split(' ')
    for palavra in frases:
        if palavra in dicionario:
            dicionario[palavra]=dicionario[palavra]+1
        else:
            dicionario[palavra]=1
    return dicionario