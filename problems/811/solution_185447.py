# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas:list,H:int,L:int) -> bool:
    """Dadas as medidas de um colchão, em formato de lista e em ordem
    crescente, a altura H e largura L de uma porta, em centímetros,
	retorna se o colchão passaria pela porta (true) ou se não passa (false)."""
    if medidas[0] <= min(H,L) and medidas[1]<= max(H,L):
        return True
    else:
        return False