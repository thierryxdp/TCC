def carros(n_pessoas, capacidade = 5):
    import math
    "Calcula quantos carros são necessários para transportar N_PESSOAS."
    return math.ceil(n_pessoas / capacidade)