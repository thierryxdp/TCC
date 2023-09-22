# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas,H,L):
    """função que dadas as medidas do colchao e a aultura e largura da porta, retorna se True se o colchão
	passa pela porta, ou False se não passa
	list, int, int -> bool""" 
    
    porta = H, L
    colchao = medidas
    
    if colchao[1] > porta[0] and colchao[1] > porta[1]:
        passa = False
        
    else:
        passa = True
    
    
    return passa