# Função que dirá se João deve comprar ou não o colchão
# medidas(largura,comprimento,profundidade) e h e l a altura e a largura da porta
def colchao(medidas,h,l):
    """Função que calcula se o colchão passa ou não na porta da casa de João"""
    """lista,float,float->bool"""
medidas=(comprimento,largura,altura)
	if largura<=h and altura<=l or largura<=l and altura<=h:
        return "True"
    else:
        return "False"