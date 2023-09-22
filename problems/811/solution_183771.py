# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''Função que diz, se uma cama passa por uma porta:
    list, int, int -> string'''
    M = str(medidas)
    B = int(M[5:8])
    if B <= H:
        return True
    else:
        return 'False'