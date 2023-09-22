def carros (pessoas, capacidade=5):
	"""função que volta o numero de carros convencionais necessarios para viagem"""
	automoveis= math.ceil(pessoas//capacidade)
    return automoveis