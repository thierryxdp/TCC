def carros(pessoas):
    """calcula e retorna a quantidade de carros necessarios dados a quantidade de pessoas e sabendo que cada carro convencional suporta 5 pessoas"""
    quantidade_pessoas_por_carro = 5
    return (pessoas//quantidade_pessoas_por_carro)