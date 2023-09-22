def conta_frases(texto):
    '''Conta o numero de frases que aparecem no texto.
    str-->int'''
    qnt = 0 
    i = 0
    pontuacao = ['!','.',':','...','?']
    frases = texto.split()
    while i < len(frases):
        if pontuacao in frases[i]:
            qnt = qnt + 1
        	i = i + 1
    	return qnt