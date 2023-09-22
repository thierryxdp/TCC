def posLetra(frase,letra,ocorrencia):
    """funcao que retorna a posicao da ocorrencia determinada de uma letra dada de uma frase; str,int->int"""
    i=0
	ind=[]
    if str.count(frase,letra)<ocorrencia:
        return -1
	else:
        while i<len(frase):
			if letra in frase[i]:
				ind=ind+[i]
			i=i+1
		return ind[(ocorrencia-1)]