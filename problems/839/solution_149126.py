import math

def carros(p,c=5):
    """Calcula e retorna o valor de carros necessários para a viagem.
	Temos como parâmetro de entrada: P quantidade de pessoas, C capacidade
	do carro. Utilizar o valor 5 como default quando a segunda
	entrada não for especificada."""
    return math.ceil(p/c)