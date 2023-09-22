# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Função que recebe uma lista com as dimensões do colchão em centtímetros, ordenadas da menor para a maior, e dois inteiros H e L e retorna True se colchão passa pela porta e False se ele não passa."""
    if medidas[0] > H or (medidas[1] > H and medidas[2]>L):
        return False
    else:
        return True