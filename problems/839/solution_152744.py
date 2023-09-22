def carros(pessoas,capacidade=5):
	CarrosNec = pessoas//capacidade + 1 - 0**(pessoas%capacidade)
	return CarrosNec