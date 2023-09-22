def freq_palavras(frases):
    """função recebe uma string como chave e 
    retorna um dicionario"""
    palavras= str.split(frases)
    dic={}
    for palavra in palavras:
       	if palavra not in dic:
           	dic[palavra]=1
       	else:
           	dic[palavra]=dic.get(palavra)+1
	return dic