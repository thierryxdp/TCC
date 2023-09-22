def colchao(medidas,H,L):
	'''retorna se o colçhao dado as medias em lista A,B,C
	e a largura L e altura H da porta,  vai passar
    list,float,float->bool'''
   #obs:A<B<C L<H
    s=medidas
    if s[2]<L:
    	return s[2]<L
	elif s[1]<L and s[2]<H:
        return s[1]<L and s[2]<H
    elif s[1]<H:
        return s[1]<H
    elif s[1]<L:
        return s[1]<L
    else:
        return False