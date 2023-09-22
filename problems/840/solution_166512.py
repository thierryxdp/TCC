def bolos(A,B,C):
    """A FUNCAO CALCULA A QUANTIDADE DE BOLOS DADOS SEUS NUMEROS DE ENTRADA"""
    Quant_Farinha = A/2
    Quant_Ovos = B/3
    Quant_Leite = C/5
    bolo = min(Quant_Farinha,Quant_Ovos,Quant_Leite)
    return int(bolo)