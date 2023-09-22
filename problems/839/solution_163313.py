def carros(num_passageiros,quant_carros):
    """Função que calcula a quantidade de carros que são necessárias para realizar uma viangem dado um numero x de passageiros
    INT, INT -> INT"""
    C= quant_carros
    if num_passageiros<= 5:
        return 1
    else:
        viagens = num_passageiros // C
    return viagens