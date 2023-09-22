def freq_palavras(frases):
    """
"""
    frases = str.split(frases)
    dic = {}
    for palavras in frases:
        if palavras in dict.keys(dic):
            dic[palavras] += 1
        else:
            dic[palavras] =1
    return dic