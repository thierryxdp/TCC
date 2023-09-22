def posLetra(frase,letra,numero):
    ocorrencia=0
    pos=0
	for i in range(len(frase)):
        if frase[i] == letra:
            ocorrencia+=1
            if ocorrencia==numero:
                pos=i
			else:
                pos=-1
    return pos