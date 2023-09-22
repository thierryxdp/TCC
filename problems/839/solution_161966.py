def carros(num_pessoas, capacidade = 5):
    """Função que recebe o número de pessoas e a capacidade dos carros caso o seu valor
    seja não conveniente (capacidade = 5)
    Entrada: int
    Saída: 
    """
    num_carros = num_pessoas // capacidade
    return num_carros