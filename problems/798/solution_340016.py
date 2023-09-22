def freq_palavras(frases):
    """retorna um dicionario onde cada palavra de frases é uma chave que tem como valor o número de vezes que a palavra aparece. str -> dict"""
    a= str.split(frases)
    dicio={}
    for palavra in a:
        if palavra not in dicio:
            dicio[palavra]=1
        else:
            dicio[palavra]+=1
    return dicio