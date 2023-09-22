def carros(pessoas, capacidade=5):
    if capacidade == 5:
    	total = pessoas//capacidade 
    else:
    	total = (pessoas//capacidade)+1
    
    return total