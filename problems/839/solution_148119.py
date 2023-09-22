def carros(pessoas, capacidade=5):
    """ Esta função retorna calcular e retornar o número exato de carros necessários para esta viagem, dado o número de pessoas e a capacidade de cada carro.
    	int, int -> int.
        
        Parameters:
            pessoas: número de pessoas que vão na viagem
            capacidade: número de pessoas que cabem em cada carro, considerando que todos os carros comportam o mesmo número de pessoas. Argumento só é necessário caso a capacidade seja diferente de 5, já que esse é o valor default.
    """
    return int(pessoas/capacidade)