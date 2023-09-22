def posLetra(s,l,n):
    contador = 0
    while contador < n:
    	a = s.find(l)
        s.replace(s[a],'#',1)
    	contador = contador + 1
    return a