def carros(x):
    """dado o numero de pessoas, retorna quantos carros serão necessários para a viagem com um carro que comporta até 5 pessoas.
    Entrada: int
    Retorno: int"""
    if x<=5:
        return 1
    else:
        return math.ceil(x/5)