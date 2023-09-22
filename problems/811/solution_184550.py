# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Função que verifica se é ou não possível passar um colchão pela
       porta dadas suas dimensões
       
       Parameters:
       medidas: lista contendo os tamanhos inteiros A, B e C do colchão
       H: Medida da altura da porta
       L: Medida da largura da porta
       
       returns:
       Retorna se o colchão pode ou não passar pela porta da casa
       list, int, int -> bool
       """
    if medidas[1]<=H:
        return True
    else:
        return False