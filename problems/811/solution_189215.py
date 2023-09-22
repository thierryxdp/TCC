# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(A,B,C=lista,H,L):#maneira simples e direta(mais compacta)
    '''Função que dados as dimensões do colchão(A,B,C)
informa se aquele colchão consegue passar pela porta(H,L)
ambos medidos em centímetros.
float,float,float,float,float->bool'''
    if H>=A and L>=B or H>=B and L>=A or H>=C and L>=C:
        return true
    else:
        return false