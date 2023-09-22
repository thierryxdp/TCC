def conta_frases(frase):
    '''Função que pega a frase de entrada e retorna quantas frase tem de acordo com a pontuação 
    str,str→int'''
   	list2 = []
	pontuacao=['...','!','?','.']
	pontuacao1= text.split(pontuacao[0])
	print(pontuacao1)
	for i in pontuacao1:
    	for x in pontuacao:
        	z = i.split(x)
        	list2.append(z)
	return len(list2)/2)