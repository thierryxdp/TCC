def conta_frases(texto):
	'''Função retorna a quantidade de frases em um texto
       str --> int'''
    numero = 0 
    if '.' in texto:
        numero+= texto.count('.') - (3*texto.count('...'))
    if '...' in texto:
        numero+= texto.count('...')
    if '?' in texto:
        numero+= texto.count('?')
    if '!' in texto:
        numero+= texto.count('!')
    return numero