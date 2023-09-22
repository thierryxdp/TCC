# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if medidas[1] <= H or medidas[2] <= L:
        return True
    else:
        return False
    '''retorna um valor verdadeiro ou falso do problema apresentado
    definido pela medidas 1 e madidas 2'''