def inverte(frase):
    ''' Essa função inverte a frase, retirando toda pontuação e adicionando um espaço no local,
    depois retorna um a frase com as alterações'''
    if ':' in frase:
        frase= frase.replace(':',' ')
    if ',' in frase:
        frase= frase.replace(',',' ')
    if '.' in frase:
        frase= frase.replace('.',' ')
    if '!' in frase:
        frase= frase.replace('!',' ')
    if '?' in frase:
        frase= frase.replace('?',' ')
    if '-' in frase:
        frase= frase.replace('-',' ')
    if ';' in frase:
        frase= frase.replace(';',' ')
    f1 = frase.split(" ")
	f2 = len(f1)+1
	f3 = f1[-1:-(f2):-1]
	inverter = str.join(’ ’,'f3')
	return inverter