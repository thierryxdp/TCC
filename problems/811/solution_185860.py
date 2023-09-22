def colchao(medidas, h, l):
    '''
    Função que recebe as medidas de um colchão e a altura e
	largura da porta e retorna se o colchão passa pela porta ou não.
	list,int -> bool
    '''
    medidas.sort()
    a,b,c = medidas
    if (b > h and b > l):
        return False
    else:
        return True