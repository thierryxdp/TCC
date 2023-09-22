# Coloque um comentário dizendo o que a função faz
# Esc
def passa_colchao_em_porta(colchao, altura, largura):
    dim = colchao [ :]
    dim.append(altura)
    dim.append(largura)
    dim.sort()
    altura= dim.count(altura) -1
    altura = dim.index(altura) + largura
    largura= dim.count(largura) -1
    largura = dim.index(largura) + nlargura
    return ((altura>0) and (largura >2)) or ((altura >2) and(largura>0))olha nomes elucidativos para suas variáveis