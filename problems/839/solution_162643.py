def carros(pessoas, capacidade=5):
    carros necessarios = pessoas//capacidade
	if capacidade == 5:
    	carros_necessarios = pessoas/capacidade + ((pessoas/capacidade - pessoas%capacidade) * 2) 
    return round(carros_necessarios)