def tirar_Minus(expressao):
	a=expressao
    a=a.replace('!',' ')
    a=a.replace('?',' ')
    a=a.replace(':',' ')
    a=a.replace(';',' ')
    a=a.replace('.',' ')
    a=a.replace(',',' ')
    a=a.replace('-',' ')
	a=a.lower()
    return a

def inverte(expressao):
    b=tirar_Minus(expressao)
    a = b.split(' ')
    a.reverse() 
    return ' '.join(a)