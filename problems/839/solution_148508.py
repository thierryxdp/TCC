def carros(x, cv=5):
    """calcula o numero necessario de carros para uma viagem, dados o numero de passageiros e a capacidade do veiculo, caso essa nao for informada, a capacidade sera de 5 passageiros
    parametros:
    x: numero total de pessoas
    cv: capacidade do veiculo
    """
    """int, int --> int"""
    if x//cv:
        return x//cv+ 1
    else x//cv:
        return x//cv