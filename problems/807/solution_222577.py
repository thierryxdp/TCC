def conta_frases(text):
    '''Conta a quantidade de frases que um texto tem; recebe
    como parâmetro um texto dado por um usuário.String-->Int'''
	if('...' in text):
        return str.count(text,'.')+str.count(text,'!')+str.count(text,'?')+str.count(text,'...')-3*str.count(text,'...')
    else:
        return str.count(text,'.')+str.count(text,'!')+str.count(text,'?')