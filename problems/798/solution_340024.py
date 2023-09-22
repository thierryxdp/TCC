def freq_palavras(frases):
    
    palavras = str.split(frases)
    dic = {}
    for palavra in palavras:
        dic[palavra] = list.count(palavras, palavra)
    return dic