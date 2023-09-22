def freq_palavras(frases):
    """Função que cria um dicionário de palavras-chave e
       suas respectivas frequências/valores.
"""
	li1 = str.split(frases,' ')
    dic = {}
    for x < len(li1):
    	dic[li1[x]] = dict.get(dic, dic[li1[x]], 0) + 1
    return li1[0]