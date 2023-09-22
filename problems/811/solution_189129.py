# Função que dirá se João deve comprar ou não o colchão
# medidas(largura,comprimento,profundidade) e h e l a altura e a largura da porta
def colchao(medidas,h,l):
    """Função que retorna true se o colchão passar pela porta e false se não passar"""
    """lista,float,float->bool"""
	 medidas[0]<=h and medidas[1]<=l or medidas[0]<=l and medidas[1]<=h