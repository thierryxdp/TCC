def conta_frases(texto):
	numero = 0 
    if '. ' in texto:
        numero+= texto.count('. ')
    if '...' in texto:
        numero+= texto.count('...')
    if '?' in texto:
        numero+= texto.count('?')
    if '!' in texto:
        numero+= texto.count('!')
    return numero