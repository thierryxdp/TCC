def carros (pessoas, capacidade=5):
    """ funcao que retorna o numero de carros dependendo da quantidade de pessoas"""
    if pessoas == 0:
        return 0
    elif pessoas < capacidade or pessoas == capacidade and pessoas !=0:
        return 1
    else: pessoas % capacidade !=0
        return (pessoas//capacidade)+1