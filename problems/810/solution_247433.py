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
    frase1 = frase.split(' ')
	inverso = frase1[::-1]
	return str.lower(inverso)