# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(m,h,l):
    '''Dado as dimensões do colchão, a altura da porta e a largura da porta,
    retorna se você consegue ou não passar com o colchão.
    list,int,int --> bool'''
    A= m[0]
    B= m[1]
    C= m[2]
    if A*B <= h*l :
        return True
    else:
        return False