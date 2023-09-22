# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """ dadas as medidas, em cm, do colchao, da altura e da largura retorna se Joao conseguira passar o colchao pela porta de casa;
    ent-> tupla, int, int
    saida-> bool"""
    A=tuple[1]
    B=tuple[2]
    C=tuple[3]
    
    if C>H or B>L:
        return False
    else:
        return True