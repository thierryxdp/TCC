def carros(pessoa,capacidade):
    """Retorna a quantidade de veiculos para uma viagem:
    int, int ->int"""
    if pessoa>capacidade:
        return int(pessoa/capacidade)