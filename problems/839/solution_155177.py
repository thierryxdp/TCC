def carros(pessoas,capacidade=5):
    """Retorna a quantidade de carros necessarios para a viagem;
    	int,int -> int"""
    return round(pessoas/capacidade+0.4)