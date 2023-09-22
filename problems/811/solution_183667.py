# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """ dadas as medidas, em cm, do colchao, da altura e da largura retorna se Joao conseguira passar o colchao pela porta de casa;
    ent-> int, int, int
    saida-> bool"""
    A=(medidas[:2])
    B=(medidas[3:5])
    C=(medidas[6:])
    return H>C and L>B