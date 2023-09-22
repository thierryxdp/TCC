def maiores(lista_numeros, n):
    a= list.sort(lista_numeros)
    if n in lista_numeros:
    	b= list.index(lista_numeros,n)
    	c= lista_numeros[(b+1):]
    	d= list.count(c,n)
    	e= c[(0+d):]
    	return e
    elif f==6:
        b= list.index(lista_numeros,f)
        c= lista_numeros[(b+1):]
    	d= list.count(c,f)
    	e= c[(0+d):]
        return e
    elif f==7:
        b= list.index(lista_numeros,f)
        c= lista_numeros[(b+1):]
    	d= list.count(c,f)
    	e= c[(0+d):]
        return e
    elif f==8:
        b= list.index(lista_numeros,f)
        c= lista_numeros[(b+1):]
    	d= list.count(c,f)
    	e= c[(0+d):]
        return e
    elif f==9:
        b= list.index(lista_numeros,f)
        c= lista_numeros[(b+1):]
    	d= list.count(c,f)
    	e= c[(0+d):]
        return e
    elif f==10:
        b= list.index(lista_numeros,f)
        c= lista_numeros[(b+1):]
    	d= list.count(c,f)
    	e= c[(0+d):]
        return e
    else:
        return []

def acima_da_media(lista_de_notas):
    a= list.count(lista_de_notas,5)
    b= maiores(lista_de_notas,5) + [5,]*a
    c= list.sort(b)
    return b