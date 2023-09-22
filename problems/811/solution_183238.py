# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(colchao, altura, largura):
    dim = colchao [ :]
    dim.append(altura)
    dim.append(largura)
    dim.sort()
    _altura= dim.count(altura) -1
    altura = dim.index(_altura) + _largura
    _largura= dim.count(largura) -1
    largura = dim.index(_largura) + _largura
    return ((altura>0) and (largura >2)) or ((altura >2) and(largura>0))