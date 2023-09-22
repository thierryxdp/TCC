def freq_palavras(frases):
    """Função que recebe uma string como chave e retorne um dicionario onde cada palavra seja uma chave e quantas vezes a palavra aparece; str->dict"""
    
    palavras=str.split(frases)
    dic={}
    
    for palavras in palavras:
    	if palavra not in dic:
            dic[palavra]=1
    	else:
            dic[palavra]=dic.get(palavra)+1
                	return dic