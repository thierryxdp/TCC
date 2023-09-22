# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    '''Função que recebe as medidas de um colchão em uma lista e os valores separados
    da altura e largura de uma porta, e verifica se tal colchão passa por ela
    [lista], float, float -> bool'''
    a, b, c = medidas
    return (a <= H and b <= L) or (a <= L and b <= H) or (a <= H and c <= L) or (a <= L and c <= H) or (c <= H and b <= L) or (c <= L and b <= H)