def melhor_volta(matriz):
    voltas=[]
	b=0   
    for linha in matriz:
        melhor=min(linha)
        list.append(voltas, melhor)
        if min(voltas) in linha:
            a=matriz.index(linha)
        for melhor in linha:
            if linha==a:
            	b=linha.index(melhor)+1
            
	return (a+1,min(voltas),b)