def substitui(s,x,i):
	'''função que substitui caracter na posição i por caracter x
    str, int, int -> str'''
    y=i+1
    return s[:i]+x+s[y:]