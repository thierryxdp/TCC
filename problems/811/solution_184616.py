# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """função que retorna se o colchão pode ou não passar pela porta, sendo dadas asmedidas do
   colchão e da porta, True, passa; False, não passa.
   Entrada: list, in, int
   Saída: bool"""
    if medidas[1]<= H:
        return True 
    elif medidas[1]> L and H: 
        return False
    elif medidas[1]> L and medidas[1]<H:
        return True