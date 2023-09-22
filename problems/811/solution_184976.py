def colchao(medidas,H,L):
    """Função que calcula se um determidado colchão passa pela parta ou não, de acordo com as suas medidas.
    	medidas: uma lista com as dimensões do colchão em centímetros, ordenadas da menor para a maior. Devem ser inseridas entre colchetes.
        H: número inteiro correspondente á altura da porta em centímeros
        L: número inteiro correspondente á largura da porta em centímeros
 		A função retornará true se o colchão passar pela porta e False se o colchão não passar.  
   		list, float, int -> bool"""
    if (medidas[0] <= L and medidas[1] <= H):
        return True
    elif (medidas[0] <= H and medidas[1] <= L):
        return True
    else:
        return False