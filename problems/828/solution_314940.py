def primo(numero):
    """Função que calcula se um número é primo ou não"""
    """Parâmetro de entrada: int"""
    """Parâmetro de saída;int"""
    for elemento in range(2,numero):
    	if elemento % range(2,numero)==0:
			return False
    return True