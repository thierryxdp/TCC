# Função que irá comparar as medidas da porta de João (altura = H e largura = L) com as medidas do colchão que ele quer comprar (A x B x C) para analisar se o colchão passa pela porta ou não.
# medidas, H, L

def colchao(medidas:list, H:float, L:int):
    """Parameters:
    	medidas: uma lista com as dimensões do colchão em centímetros, ordenadas da menor para a maior
        H: número inteiro correspondente á altura da porta em centímeros
        L: número inteiro correspondente á largura da porta em centímeros
    
    	Returns:
        True se o colchão passa pela porta e False se o colchão não passa pela porta  
    """

    if (medidas[1] < L and medidas[2] < H):
        return True
    elif (medidas[1] < H and medidas[2] < L):
        return True
    else:
        return False