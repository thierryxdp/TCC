def conta_frases(Palavra_chave):
	"""Função que retorna a Quantidade de frases de um texto guardado numa string.
    entr:str
    saida:inteiro"""
	#

	resp=(str.replace(str.replace(str.replace(str.replace(Palavra_chave,'...','#'),'.','#'),'!','#'),'?','#'))
	conta=(resp.count('#'))
	b=resp.count('###')
	Resp=()
	if b==0:
		Resp+=(conta,)
	if b>0:
		Resp+=((conta)-(b*2),)
	return Resp[:]