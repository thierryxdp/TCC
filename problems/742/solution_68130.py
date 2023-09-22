def substitui(s,x,i):
    '''
    substitui x da string s em posição i.
    str, str, int -> str
    '''
	b = bytearray(s)
	b[2] = 'm'
	s = str(b)
	print(s)