def carros(num_pessoas,numero_de_pessoas_por_veiculo=5):
    """função que ira calcular o numero de carros necessarios
    para transportar um determinado numero de pessoas
    int,int = int
    """
    qtdcarros = num_pessoas/numero_de_pessoas_por_veiculo
    return qtdcarros