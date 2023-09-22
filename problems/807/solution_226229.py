def conta_frases(Palavra_chave):
	"""Função que retorna a Quantidade de frases de um texto guardado numa string.
    entr:str
    saida:inteiro"""
	#

	conta=(str.replace(str.replace(str.replace(str.replace(Palavra_chave,'.','#'),'!','#'),'?','#'),'...','#'))
	conta1=(('#' in conta),('###' in conta))
	lixo=(conta.count('#'))
	b=(conta.count('###'))

	if ('###' in conta):
		return(lixo-2)
	elif b==0:
		return int(lixo)