def posLetra (frase,letra,posicao):
    aparicoes=[]
    i=0
    while len(aparicoes)<posicao:
        if frase[i]==letra:
            aparicoes= aparicoes + [i]
    	i=i+1
		return aparicoes[-1]
    if len(aparicoes)!=3:
        return -1