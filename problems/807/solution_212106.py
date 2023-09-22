def conta_frases(texto):
	"""Recebe um texto e retorna a quantidade de frases baseado nos pontos/string->int"""
   	if (any(char.isdigit() for char in texto))==True:
        print("Palavras não contém números")
    else:
   		j=0
        k=0
        texto=texto.ljust(5)
        for i in range(len(texto)):
       		if(texto[0]=="." or texto[0]=="?" or texto[0]=="!"):
       			print("O texto não pode começar com pontos")
       			break
       		elif texto[i]=="." and texto[i+1]=="." and texto[i]=="."):
        		j+=1
       		elif((texto[i]=="." and texto[i+1]!="?" and texto[i+i]!="!" and texto[i+3]!=".")or(texto[i]=="?" and texto[i+1]!="."and texto[i+1]!="?" and texto[i+i]!="!")or(texto[i]=="!" and texto[i+1]!="."and texto[i+1]!="?" and texto[i+i]!="!")):
            	k+=1
		return j+k