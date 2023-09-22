# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Função que verifica se é possível passar um colchão de dimensões A x B x C
    por uma porta de altura H e largura L. Os dados são introduzidos em uma tupla
    no seguinte formato:
    ([medida_A,medida_B,medida_C],H,L)
    Devendo as medidas A, B e C estar em ordem crescente
    tuple(list,float,float)->bool"""
    medidas_colchao=colchao[0]
    a_colchao=medidas_colchao[0]
    b_colchao=medidas_colchao[1]
    c_colchao=medidas_colchao[2]
    deitado_lmaior=a_colchao<L and b_colchao<H
    return deitado_lmaior