def colchao(medidas,H,L):
    """dado uma lista com as medidas do colchão e dois inteiros com altura e largura da porta respectivamente, a função reornar True se for possivel passar ou False se não for possivel a  passagem do colchão pela porta;
	list, int, int-> bool"""
    altura=[H]
    largura=[L]
    if medidas[1:2] > altura and medidas[1:2] > largura and medidas[2:] > altura and medidas[2:] > largura:
        return False
    else:
        return True