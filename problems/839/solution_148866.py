from math import ceil
def carros(numero,capacidade):
    """Funcao que calcula e retorna o numero de carros necessarios para 
    a viagem.
    Entrada: int,int 
    Saída: int
    """
    if capacidade>0: 
        return ceil(numero/capacidade)
    else:
        return ceil(numero/5)