def freq_palavras(frases):
    """Função que cria um dicionário de palavras-chave e
       suas respectivas frequências/valores.
"""
    li1 = str.split(frases,' ')
    dic = {}
    con = 0
    for x in range(0,len(li1)+1,1):
        if frases[x] in dic:
            dic[x] = dict.get(dic, dic[x], 0) + 1
    return dic