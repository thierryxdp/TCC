def primo(numero):
	"""retorna um valor inteiro dado um valor
    int->bool"""
    indice=1
    lista=[]
    while indice<=numero:
        if numero%indice==0:
            lista=lista+[indice]
            indice=indice+1
		else:
            indice=indice+1
        if len(lista)==2:
			return True
        else:
            indice=indice+1
        if len(lista)==2:
            return False