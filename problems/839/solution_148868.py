from math import ceil
def carros(numero,capacidade=5):
    """Funcao que calcula e retorna o numero de carros necessarios para 
    a viagem.
    Entrada: int,int 
    Saída: int
    """
    if capacidade>0: 
        return ceil(numero/capacidade)
    else:
        capacidade = 5
        return ceil(numero/capacidade)