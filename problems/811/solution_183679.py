# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """ dadas as medidas, em cm, do colchao, da altura e da largura retorna se Joao conseguira passar o colchao pela porta de casa;
    ent-> tupla, int, int
    saida-> bool"""
    A=int(medidas[:2])
    B=int(medidas[3:6])
    C=int(medidas[7:])
    pra n entrar
    if C>H or B>L:
        return False
    else:
        return True