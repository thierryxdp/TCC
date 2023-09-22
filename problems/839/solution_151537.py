def carros(pess,cap):
	"""Função que recebe o número de pessoas (pess), a
    capacidade do carro (cap) ou considera o veículo convencional
    e retorna o número de carros para a viagem
    int, int -> int """
    if cap==True:
    	carros=(pess//cap)
		if (pess%cap)>0:
        	carros+=1
    if cap==False:
        carros=(pess//5)
        if (pess%5)>0:
        	carros+=1
    return carros