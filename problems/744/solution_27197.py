def hashtag(s):
    '''Função que insere o caractere # no inicio, meio e fim da string recebida'''
	a =(s.count('')-1)
	valor_medio = a//2
    final = '#'+s[0:valor_medio] + '#' + s[valor_medio:] + '#'
    return final