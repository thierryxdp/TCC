m = [["Alberto Ferreira", "366", "Contabilidade", "(21)84567-5248"], ["Juliana Vasconcelos", "456", "RH", "(21)3553-88766"], ["Flavia Amorim", "365", "Contabilidade", "(21)2156-4664"]]

def busca(setor, matriz):
	ret = []
	for arr in matriz:
		if setor in arr:
			ret.append([arr[0], arr[1], arr[2]])
	return ret