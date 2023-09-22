def freq_palavras(frases):
    """Retorna um dicionário onde cada palavra dessa string seja uma chave e 
       tenha como valor o número de vezes que cada palavra aparece. str-> dict"""
    dicio={}
    s = str.split(frases)
    for a in s:
        dicio[a]= str.count(s,a)
    return dicio