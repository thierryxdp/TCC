def carros(x,y = 1):
    """dado o numero de pessoas, retorna quantos carros serão necessários para a viagem com um carro que comporta até 5 pessoas.
    Entrada: int
    Retorno: int"""
    if x <=5 and != 0:
        return 1
    else:
        return math.ceil(x/5)