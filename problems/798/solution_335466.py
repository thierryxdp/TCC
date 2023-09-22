def freq_palavras(frases):
    """Retorna um dicionário onde cada palavra dessa string seja uma chave e 
       tenha como valor o número de vezes que cada palavra aparece. str-> dict"""
    dicio={}
    for a in frases:
        dicio[a]= str.count(frases,a)
    return dicio