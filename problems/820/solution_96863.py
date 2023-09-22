def posLetra (frase,letra,ocorrencia):
    aparicoes=[]
    i=0
    while len(aparicoes)<ocorrencia:
        print(frase[i])
        if frase[i]==letra:
            aparicoes= aparicoes + [i]
    	i=i+1
		return aparicoes[-1]