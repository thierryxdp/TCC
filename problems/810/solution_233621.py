def inverte(frase):
    '''Retorna uma frase na ordem inversa da original e sem pontuação;
    str -> str'''
    s=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'.',' '),'...',' '),'?',' '),'!',' ')
	s=str.lower(str(s))
    s=str.split(s)
    s=s[::-1]
    return str.join(' ',s)