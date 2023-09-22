# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(m,h,l):
    A= m[0]
    B= m[1]
    if A*B <= h*l:
        return True
    else:
        return False