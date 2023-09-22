import math
def num_bombons(dinheiro,valor):
    """Determina a quantidada a ser comprada de tal objeto; float,float=>int """
    resp=dinheiro/valor
    resp= math.floor(resp)
    return resp