def num_bombons(dinheiro:float,preçoBombon:float):int:
    """Calcula o quantos bombons consegue comprar dados o quanto
    	dinheiro se tem e o preço do bombom
        float, float -> int"""
    quantidadeBombons = dinheiro//preçoBombon
    return quantidadeBombons