def posLetra(frase,letra, n):
    '''retorna o indice da ocrrencia n da letra na frase'''
    qtd=str.count(frase,letra)
    if qtd<=len(frase):
    	return frase.find(letra,n+1)
    else:
        return -1