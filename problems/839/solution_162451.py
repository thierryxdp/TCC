def carros(num_pessoas,capacidade=5):
    """Função que recebe o número de pessoas e a capacidade de cada veículo caso seja
    diferente do convencional.
    Entrada: int, int
    Saída: int"""
    num_carros = round(num_pessoas/capacidade,0)
    return num_carros