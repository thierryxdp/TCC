def maiores(lista_numeros, n):
    a= list.sort(lista_numeros)
    if n in lista_numeros:
    	b= list.index(lista_numeros,n)
    	c= lista_numeros[(b+1):]
    	d= list.count(c,n)
    	e= c[(0+d):]
    	return e
    elif:
        b= list.index(lista_numeros,6)
        c= lista_numeros[(b+1):]
    	d= list.count(c,6)
    	e= c[(0+d):]
        return e
    elif:
        b= list.index(lista_numeros,7)
        c= lista_numeros[(b+1):]
    	d= list.count(c,7)
    	e= c[(0+d):]
        return e
    elif:
        b= list.index(lista_numeros,8)
        c= lista_numeros[(b+1):]
    	d= list.count(c,8)
    	e= c[(0+d):]
        return e
    elif:
        b= list.index(lista_numeros,9)
        c= lista_numeros[(b+1):]
    	d= list.count(c,9)
    	e= c[(0+d):]
        return e
    elif:
        b= list.index(lista_numeros,10)
        c= lista_numeros[(b+1):]
    	d= list.count(c,10)
    	e= c[(0+d):]
        return e
    else:
        return []

def acima_da_media(lista_de_notas):
    a= list.count(lista_de_notas,5)
    b= maiores(lista_de_notas,5) + [5,]*a
    c= list.sort(b)
    return b