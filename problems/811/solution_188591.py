def colchao(m,h,l):
    '''Dado uma lista onde possui as dimensoes do colchao e
    da porta, a funcao retorna se da ou nao para passar'''
    if h>l:
        if m[1]<=h:
            return True
        else:
            return False
	else:
        if m[1]<=l:
            return True
        else:
            return False