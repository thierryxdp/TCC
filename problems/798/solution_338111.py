def freq_palavras(frases):
    """Função que cria um dicionário de palavras-chave e
       suas respectivas frequências/valores.
"""
	li1 = str.split(frases,' ')
    dic = {}
    for c in range (0, len(li1) + 1, 1):
        dic[li1[c]] = dict.get(dic, li1[c], 0) + 1
    return li1[0]