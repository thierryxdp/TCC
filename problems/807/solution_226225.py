def conta_frases(Palavra_chave):
	"""Função que retorna a Quantidade de frases de um texto guardado numa string.
    entr:str
    saida:inteiro"""
	#

	conta=(str.replace(str.replace(str.replace(str.replace(Palavra_chave,'.','#'),'!','#'),'?','#'),'...','#'))
	conta1=(('#' in conta),('###' in conta))
	lixo=(conta.count('#'))
	b=(conta.count('###'))
	
	if b!=0:
		return(lixo-b)
	elif b==0:
		return int(lixo)