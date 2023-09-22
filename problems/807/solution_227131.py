def conta_frases(texto):
    '''conta o numero de frases presente em um texto'''
    frases=0
    if'...' in texto:
        frases=+frases+str.count(texto,'...')
    if'.' in texto:
        frases=+frases+str.count(texto,'.')-3*str.count(texto,'...')
	if'!' in texto:
        frases=+frases+str.count(texto,'!')
    if'?' in texto:
        frases=+frases+str.count(texto,'?')
    
    
    
    return frases