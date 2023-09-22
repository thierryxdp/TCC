def carros (n,c=5):
    '''calcula o numero de carros necessario para transportar n pessoas de acordo com a capacidade c do carro
    se c nao for dado sera considerada a capacidade convencional de 5 pessoas por carro
    int, int -> int'''
    from math import ceil()
    return ceil(n/c)