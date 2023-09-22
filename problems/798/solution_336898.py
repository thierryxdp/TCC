def freq_palavras(frases):
	'''
	Ao inserir uma string, retornará um dicionário
	com a chave e quantas vezes ela apareceu. 
	str-> dict
	'''
    x=frases.split(' ')
    dc={}
    for i in range(len(x)):
        substring=x[i]
        frases.count(substring)
        dc[x[i]]=x.count(substring)
    return dc