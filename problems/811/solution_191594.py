def colchao(medidas,H,L):
    """Funcao que recebe como entrada uma lista com a dimensao do colchao
    e 2 valores H e L que definem a altura e a largura da porta
    e retorna em booleano se é possivel passar o colchao pela porta.
    list,int->bool"""
    if medidas[1]<=H or medidas[2]<=L:
    	return True
    else:
        return False