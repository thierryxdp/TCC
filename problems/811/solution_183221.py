# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(dimens,h,l):
    '''recebe uma lista com as dimensões do colchao e a altura e largura relativas à porta
    e retorna se o colchão passa ou nao pela porta com os valores true ou false
    list, int, int -> str'''
    x = list[dimens]
    if x.index(1) <= l and x.index(2) <= h:
        return True
    else:
        return False