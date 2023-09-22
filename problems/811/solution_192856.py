# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
'''Avalia se a segunda maior medida do colchão é menor que a maior medida da porta
e se a menor medida do colchão é menor que a base. Caso o colchão consiga passar pela porta,
retorna True e caso não, retorna False'''
def colchao(medidas,H,L):
    a, b, c = medidas[0:3]
    if H >= L:
        altura = H and base = L
    else:
        altura = L and base = H

    if b <= altura and a <= base:
        return True
    else:
        return False