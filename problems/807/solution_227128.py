def conta_frases(texto):
    '''conta o numero de frases presente em um texto'''
    if'...' in texto:
        frases=+frases+str.count(x,'...')
    if'.' in texto:
        frases=+frases+str.count(x,'.')-3*str.count(x,'...')
	if'!' in texto:
        frases=+frases+str.count(x,'!')
    if'?' in texto:
        frases=+frases+str.count(x,'?')
    return frases