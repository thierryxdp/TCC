def inverte(texto):
    '''Dado um texto, retorna a ordem das palavras invertida. str-->str'''	
	pontuacao= str.lower(texto)
    x=str.split(pontuacao)[::-1]
    y=str.join('',x)
    return y