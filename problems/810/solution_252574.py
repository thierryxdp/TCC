def tirar(expressao):
	a=expressao
    a=a.replace('!','')
    a=a.replace('?','')
    a=a.replace(':','')
    a=a.replace(';','')
    a=a.replace('.','')
    a=a.replace(',','')
	return a

def inverte(expressao):
    b=tirar(expressao)
    a = b.split(' ')
    a.reverse() 
    return ' '.join(a)