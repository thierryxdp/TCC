def colchao(medidas,H,L):
    "função que dado uma lista com três dimensões A,B E C do colchão, sendo C>B>A, a altura e largura da porta, compara suas dimensões e diz se o colchão passa na porta. Caso receba True, o colchão passa, e caso receba False, o colchão não passa."
    if L > medidas[0] and H >= medidas[3]:
        return True
    else:
        return False