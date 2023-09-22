# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
   
	altura, largura, comprimento = medidas 
    
    if largura > H and comprimento > L:
    	return False
    
    return True