def colchao(medidas, h, l):
    '''função que verifica se um colchão passa por uma porta dados as medidas de um colchão em uma lista e os valores 
    da altura (h) e largura(l) de uma porta 
    list, float, float -> bool'''
    medidas = a, b, c 
    return (a <= h and b <= l) or (a <= l and b <= h) or (a <= h and c <= l) or (a <= l and c <= h) or (c <= h and b <= l) or (c <= l and b <= h)# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis