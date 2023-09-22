def conta_frases(texto):
	"""Recebe um texto e retorna a quantidade de frases baseado nos pontos/string->int"""
	if(any(char.isdigit() for char in texto))==True:
		print("Palavra não contém números")
	else:
		j=0
		k=0
		w=0
		z=0
		texto=texto.ljust(5)
		for i in range(len(texto)):
			if texto[0]=="." or texto[0]=="?"or texto[0]=="!":
				print("Textos não podem começar por ponto")
			elif i+3<len(texto):
				if texto[i]=="." and texto[i+1]=="." and texto[i+2]==".":
					j+=1
				elif(texto[i]=="." and texto[i+1]!="!" and texto[i+1]!="?" and texto[i+1]!="."):
					k+=1
				elif(texto[i]=="!" and texto[i+1]!="!" and texto[i+1]!="?" and texto[i+1]!="."):
					w+=1
				elif(texto[i]=="?" and texto[i+1]!="!" and texto[i+1]!="?" and texto[i+1]!="."):
					z+=1                    
		return j+k+w+z