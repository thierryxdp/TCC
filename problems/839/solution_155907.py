carros(pessoas,capacidade=5):
    """Função que calcula o numero de veículos necessários para transportar todos os passageiros"""
   	if capacidade==5:
    return pessoas//5
	else:
        return pessoas//capacidade