def conta_frases(Palavra_chave):
	"""Função que retorna a Quantidade de frases de um texto guardado numa string.
    entr:str
    saida:inteiro"""
	#

	resp=(str.replace(str.replace(str.replace(str.replace(Palavra_chave,'...','#'),'.','#'),'!','#'),'?','#'))
	conta=(resp.count('#'))
	b=resp.count('###')
	
	if b==0:
		return(conta)
	if b>0:
		return((conta)-(b*2))