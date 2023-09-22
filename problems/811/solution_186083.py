def colchao(medidas, H, L):
    '''Função que recebe as medidas de um colchão em uma
    e os valores separados da altura e largura das portas
    da casa de João, e verifica se tal colchão passa por elas
    [lista], float, float -> bool'''
    a, b, c = medidas
    return (a <= H and b <= L) or (b <= H and a <= L) or (c <= H and a <= L) or (a <= H and c <= L) or (b <= H and c <= L) or (c <= H and b <= L)