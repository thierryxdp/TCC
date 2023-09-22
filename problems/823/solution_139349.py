def faltante(listaDePecas):
    """
    	Recebe uma lista de peças em que falta uma peça para estar completa.
        Retorna a peça que falta para completar o quebra cabeca.
 		list --> int
    """
	peca = 1
    ultimaPeca = listaDePecas[-1]
    while peca <= ultimaPeca:
    	if peca not in listaDePecas:
            return primeiraPeca
        peca += 1