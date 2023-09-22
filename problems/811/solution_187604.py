# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
     '''Função que recebe as medidas de um colchão em uma lista e os valores separados
    da altura e largura de uma porta, e verifica se tal colchão passa por ela
    [lista], float, float -> bool'''
    a,b,c = medidas
    if a <= H and b <= H or a <= L and b <= L or c <= H and c <= L:
        return true
    else:
        return false