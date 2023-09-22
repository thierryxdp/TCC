def inverte(frase):
	'Esta função inverte a frase para ser lida de trás pra frente.'
	'str--> str'
	travesao = str.replace(frase, '-',' ')
	virgua = str.replace(travesao, ',',' ')
	dois_pontos = str.replace(virgua, ':',' ')
	ponto_virgula = str.replace(dois_pontos, ';',' ')
	ponto_final = str.replace(ponto_virgula, '.',' ')
	esclamacao = str.replace(ponto_final, '!',' ')
	interrogacao = str.replace(esclamacao, '?',' ')
	frase_nova = interrogacao
    
	y = str.split(frase_nova)
	x = y[::-1]
	return str.join(' ', x)