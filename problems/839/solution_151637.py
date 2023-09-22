def carros(pess,cap=5):
	"""Função que recebe o número de pessoas (pess) e a
    capacidade do carro (cap), sendo 5 a capacidade padrão para veículos convencionais,
    e retorna o número de carros para a viagem.
    int, int -> int """
    carros=(pess//cap)
	if pess%cap>0:
        carros=carros+1
    return carros