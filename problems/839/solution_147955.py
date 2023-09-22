def carros(p, c=5):
    """calcula a quantidade de carros necessarios para transportar um valor p de pessoas e c a capacidade total dos veiculos"""
    return (p/c)+(p%c)