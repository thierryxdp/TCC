def tirar_Minus(expressao):
	a=expressao
    a.replace('!','')
    a.replace('?','')
    a.replace(':','')
    a.replace(';','')
    a.replace('.','')
    a.replace(',','')
	a.casefold()
    return a

def inverte(expressao):
    b=tirar_Minus(expressao)
    a = b.split(' ')
    a.reverse() 
    return ' '.join(a)