def carros(p,v=5):
    """Função que calcula e retorna a quantidade de carros necessária
    para transportar um número p de passageiros de acordo com a capacidade
    do veículo, normalmente, igual a cinco vagas"""
    return (int(p)/int(v))