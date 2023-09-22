def melhor_volta(matriz):
    voltas=[]

    for linha in matriz:
        melhor=min(linha)
        list.append(voltas, melhor)
        if min(voltas) in linha:
            a=matriz.index(linha)
        for melhor in linha:
            b=linha.index(melhor)+1
            
	return (a+1,min(voltas),b)