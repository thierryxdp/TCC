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
        frase= frase.replace('-','')
    if ';' in frase:
        frase= frase.replace(';','')
    	fraselist = frase.split(" ")
		range_list = len(fraselist)+1
		fat_inv = fraselist[-1:-(range_list):-1]
		inverso = list.join(’ ’,fat_inv)
	return inverso