def freq_palavras(frases):
    '''Dada uma frase, retorna um dicionario onde cada palavra
    dessa frase seja uma chave e tenha como valor o numero de 
    vezes que a palavra aparece
    str -> dic'''
    contagens = []
    dic ={}
    frase_dividida = str.split(frases)
    for palavra in frase_dividida:
		numero_de_aparicoes = list.count(frase_dividida,palavra)
        contagens.append(numero_de_aparicoes)
		for numeros in contagens:
        	dic[palavra] = numeros
	return dic