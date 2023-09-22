""" Cálculo das dimensões máximas de um colchão para que passe
na porta """

""" A função vai verificar cada uma das medidas do colchão
	frente a altura e largura, caso uma das duas seja maior
    o colchão passa e me retorna true. Se uma das medidas do 
    colchão for maior do que a largura ou altura, o colchão não
    passa, por isso o else genérico no final depois de todas
    as condições satisfeitas."""

def colchao(medidas,H,L):
    if medidas[1] <= L:
		return True
    if medidas[1] <= H :
        return True
    if medidas[2] <=L:
        return True
    if medidas[2] <=H:
        return True
    else:
        return False