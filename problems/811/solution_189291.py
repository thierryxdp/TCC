def colchao(medidas,H,L):
    """Comunica se o colçhão passa por uma porta, baseado na lista
    de medidas do colçhão em ordem crescente e nas medidas da
    algura e largura da porta todas em cm. (List,Int,Int->Bool)"""
    
    if int(medidas[1])<=max(H,L):
        return True
    else:
        return False