def colchao(medidas,h,l):
    '''Dadas as medidas do colchão, sendo elas A,B,C, a alturo e largura da porta, retorna se é possível ou não do colchão'''
    '''passar pela porta. int,int,int,int,int--->booleano.'''
	a,b,c= medidas
    return (a<=h and b<=l) or (a<=l and b<=h) or (a<=h and c<=l) or (a<=l and c<=h) or (c<=h and b<=l) or (c<=l and b<=h)