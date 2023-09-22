def carros(pessoa,capacidade):
    """Retorna a quantidade de veiculos para uma viagem:
    int, int ->int"""
    if pessoa>capacidade and capacidade>0:
        return pessoa/capacidade