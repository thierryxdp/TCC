def freq_palavras(frases):
    """Função que recebe uma string como chave e retorne um dicionario onde cada palavra seja uma chave e quantas vezes a palavra aparece; str->dict"""
    palavras=str.spli(frases)
    dic={}
    
    for palavra in palavras:
        if palavra not in dic:
            dic[palavras]=1
  					else:
                dic[palavra]=dic.get(palavra)+1
   	return dic