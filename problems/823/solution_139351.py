def faltante(listaDePecas):
    """
    	Recebe uma lista de peças em que falta uma peça para estar completa.
        Retorna a peça que falta para completar o quebra cabeca.
 		list --> int
    """
	peca = 1
    quantidadeDePecas = len(listaDePecas) + 1
    while peca <= quantidadeDePecas:
    	if peca not in listaDePecas:
            return peca
        peca += 1