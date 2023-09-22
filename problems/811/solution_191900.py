# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas, H, L):
    ladoA = medidas[0]
    ladoB = medidas[1]
    ladoC = medidas[2]
    lado_n_passa = 0
    
    if(ladoA > H or ladoA > L):
        lado_n_passa += 1
    if(ladoB > H or ladoB > L):
        lado_n_passa += 1
    if(ladoC > H or ladoC > L):
        lado_n_passa += 1
    
    if(lado_n_passa < 2):
    	return True
    else:
    	return False