def carros(x):
    """dado o numero de pessoas, retorna quantos carros serão necessários para a viagem
    Entrada: int
    Retorno: int"""
    if x<5:
        return 1
    else:
        return int(x/5)