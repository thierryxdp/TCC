def freq_palavras(frases):
    """recebe uma string e retorna um dicionario. str->dict"""
    dicionario{}
    frases=frases.strip()
    fraes=frases.split('')
    for palavra in frases:
        if palavra in dicionario:
            dicionario[palavra]=dicionario[palavra]+1
            else:
                dicionario[palavra]=1
                return dicionario