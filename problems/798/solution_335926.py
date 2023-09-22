def freq_palavras(frases):
    '''Recebe uma string e retona um dicionario onde cada palavra dessa string é uma chave e 
    tenha como valor do numero de vezes que a palavra aparece na string
    str -> dict'''
    dicionario={}
    frases=frases.strip()
    frases=frases.split(' ')
    for palavra in frases:
        if palavra in dicionario:
            dicionario[palavra]=dicionario(palavra)+1
        else:
            dicionario[palavra]=1
    return dicionario