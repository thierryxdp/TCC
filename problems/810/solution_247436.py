def inverte(frase):
    ''' Essa função inverte a frase, retirando toda pontuação e adicionando um espaço no local,
    depois retorna um a frase com as alterações'''
    if ':' in frase:
        frase= frase.replace(':','')
    if ',' in frase:
        frase= frase.replace(',','')
    if '.' in frase:
        frase= frase.replace('.','')
    if '!' in frase:
        frase= frase.replace('!','')
    if '?' in frase:
        frase= frase.replace('?','')
    if '-' in frase:
        frase= frase.replace('-',' ')
    if ';' in frase:
        frase= frase.replace(';','')
    frase_separada = frase.split(' ')
	frase_quantidade = len(frase_separada)+1
	frase_invertida= frase_separada[::-1]
	inverso = str.join(" ",frase_invertida)
	return str.lower(inverso)