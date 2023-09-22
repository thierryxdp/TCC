def conta_frases(Palavra_chave):
	"""Função que retorna a Quantidade de frases de um texto guardado numa string.
    entr:str
    saida:int"""
	vmsLa=(str.split(Palavra_chave,"."))
	vmsL1=(str.split(Palavra_chave,"!"))
	vmsLb=(str.split(Palavra_chave,"?"))
	vmsl2=(str.split(Palavra_chave,"..."))
	conta=(len(vmsLa),len(vmsL1),len(vmsLb),len(vmsl2),)

	return  (conta)