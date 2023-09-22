def carros(pessoas=0,veiculo=5):
    """função que calcula e retorna o número exato de carros necessários para a viagem dado o número de pessoas que irão viajar e a capacidade dos carros."""
    return int(pessoas/veiculo) + 1