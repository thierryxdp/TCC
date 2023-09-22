def posLetra(frase,letra,ocorrencia):
    """funcao que retorna a posicao da ocorrencia determinada de uma letra dada de uma frase; str,int->int"""
    i=0
	ind=[]
	while i<len(frase):
		if letra in frase[i]:
			ind=ind+[i]
		i=i+1
	return ind[(ocorrencia-1)]