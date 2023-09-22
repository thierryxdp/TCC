def freq_palavras(frases):
    """Cria uma lista separando a string pelos espaços, verificando para
    cada palavra da lista se ela está ou não no dicionário. Não estando,
    adiciona ela e atribiu a 1 como valor da palavra, caso já esteja
    no dicionário, soma 1 ao valor antes correspondente a palavra.
	str-> dicionário"""
    palavras=frases.split()
    quant_palavra={}
    for palavra in palavras:
        if palavra in quant_palavra:
            quant_palavra[palavra]+=1
        else:
            quant_palavra[palavra]=1
    return quant_palavra