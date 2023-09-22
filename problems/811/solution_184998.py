# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(mcol,h,l):
    '''Entre com uma lista com as medidas do colchao e as medidas da porta
    Lista, Int, Int - Bool'''

    if h>=mcol[1] or mcol[2]<=l:
        return True

    else:
        return False