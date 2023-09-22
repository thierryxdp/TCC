# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(a,b,c,h,l):
    '''recebe uma lista com as dimensões do colchao e a altura e largura relativas à porta
    e retorna se o colchão passa ou nao pela porta com os valores true ou false
    list, int, int -> str'''
    lista_1 = [a,b]
    lista_2 = [l,h]
    if a <= l and b <= h:
        return True
    else:
        return False