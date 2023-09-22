from math import ceil
def carros(p,c=5):
    """Funcao que calcula o numero exato de carros necessarios para realizar uma viagem, dado o numero de pessoas(p) e a capacidade do veiculo(c);
    	int, int -> int"""
    return ceil(p/c)