# Função que dirá se João deve comprar ou não o colchão
# medidas(largura,comprimento,profundidade) e h e l a altura e a largura da porta
def colchao(medidas,h,l):
    """Função que calcula se o colchão passa ou não na porta da casa de João"""
    """lista,float,float->bool"""
	if medidas[0]<=h and medidas[1]<=l or medidas[0]<=l and medidas[1]<=h:
         return True
    else:
        return False