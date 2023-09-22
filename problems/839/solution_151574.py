def carros(pess,cap):
	"""Função que recebe o número de pessoas (pess) e a
    capacidade do carro (cap) e retorna o número de carros para a viagem
    int, int -> int """
    carros=(pess//cap)
	if pess%cap>0:
        carros=carros+1
    return carros

def carros(pess):
	"""Função que recebe o número de pessoas (pess)
    e retorna o número de carros para a viagem
    int -> int """
    carros=(pess//5)
	if pess%5>0:
        carros=carros+1
    return carros