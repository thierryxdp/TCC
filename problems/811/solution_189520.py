# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(Dimensoes, H, L):
    """Função que dadas as dimensões de um colchão em centímetros, verifica se é possível passá-lo pela porta da casa.
    Parâmetros de Entrada: List, Int, Int
    Valor de Saída: Bol """
        
    if ((Dimensoes[0] <= H or Dimensoes[0] <= L) and (Dimensoes[1]<=H or Dimensoes[1]<=L)) or  ((Dimensoes[0] <=H or Dimensoes[0] <=L) and (Dimensoes[2]<=H or Dimensoes[2]<=L)):
        return True
    else:
        return False