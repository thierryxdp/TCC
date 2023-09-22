def posLetra (frase,letra,ocorrencia):
    aparicoes=[]
    i=0
    while len(aparicoes)<ocorrencia:
        
        if frase[i]==letra:
            aparicoes= aparicoes + [i]
        i=i+1
		print(frase[i])
      	return aparicoes[-1]