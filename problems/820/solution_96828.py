def posLetra (frase,letra,posicao):
    aparicoes=[]
    i=0
    while len(aparicoes)<3:
        if frase[i]==letra:
            aparicoes= aparicoes +[i]
        i+=1
    	return aparicoes[2]
    else:
        return -1