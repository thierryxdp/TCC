# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    '''Funcao que indica se o colchao passa pela porta.
    lista, int, int -> Booleana'''
    if medidas[1] <= H:
        return True
    else:
        return False