def posLetra(frase,letra,numero):
	'''Passou em 7 somente'''
    i=0
    posicao=0
    x=0
    if frase.count(letra)>=numero:
        while i<numero:
            if frase[posicao]==letra:
            	x+=1
            i+=1
        return x-1
    else: 
        return -1