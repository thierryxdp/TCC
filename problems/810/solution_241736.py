def inverte(texto):
    '''Dado um texto, retorna a ordem das palavras invertida. str-->str'''	
	pontuacao= str.lower(retira_pontuacao(texto))
    x=str.split(pontuacao)[::-1]
    y=str.join('',x)
    return y