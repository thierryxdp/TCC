def carros(pessoas, capacidade=5):
	if capacidade == 5:
    	carros_necessarios = pessoas/capacidade + ((pessoas/capacidade - pessoas%capacidade) * 2) 
	carros necessarios = pessoas//capacidade        
    return round(carros_necessarios)