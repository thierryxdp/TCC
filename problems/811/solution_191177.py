def colchao(medidas,h,l):
    '''Função que calcula e retorna se determinado colchão para na porta, dado as medidas do colchão, altura e largura da porta; list,int,int -> bool'''
	colchao=medidas[1]
    if colchao>h:
        return False
    else:
        return True