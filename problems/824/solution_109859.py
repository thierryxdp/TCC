def uppCons(frase):
    "Torna todas as consoantes da frase maiúsculas."
	listafrase=list(frase)
	def maiusculador(letra):
            if letra.lower() not in ['a','e','i','o','u','ã','â','é','ó','ô','í','ú']:
				Letra=letra.upper()
				return(Letra)
			else:
				return(letra)  
	listafraseres=list(map(maiusculador,listafrase))
	return(''.join(listafraseres))