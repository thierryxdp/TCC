def conta_frases(texto):
	'''Funcao que, dado um texto, retorna o numero de frases contidas no texto, sendo ponto final, exclamacao,interrogacao ou tres pontos em sequencia os elementos que finalizam a frase (pontos de interrogacao e exclamacao nao aparecerao repeetidos em sequencia; str -> int'''
    x=frases
    str.replace(texto,'...','?')
    if '?' in texto:
        x= str.count(texto,'?')
    if '.' in texto:
        x= str.count(texto,'.')
    if '...' in texto:
        x= str.count(texto,'...')
    if '!' in texto:
        x= str.count(texto,'!')
    return frases