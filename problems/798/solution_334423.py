def freq_palavras(frases):
    '''Dada uma frase, retorna um dicionario onde cada palavra
    dessa frase seja uma chave e tenha como valor o numero de 
    vezes que a palavra aparece
    str -> dic'''
    contagens = []
    dic ={}
    elementos = str.split(frases)
    for palavra in elementos:
		qntd = list.count(elementos,palavra)
        contagens.append(qntd)
		for numeros in contagens:
        	dic[palavra] = numeros
	return dic