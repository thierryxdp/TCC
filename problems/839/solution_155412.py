def carros(pessoas=0,capacidade=5):
    """função que calcula e retorna o número exato de carros necessários para a viagem dado o número de pessoas que irão viajar e a capacidade dos carros."""
	veiculo = math.ceil(pessoas/capacidade)
    return veiculo