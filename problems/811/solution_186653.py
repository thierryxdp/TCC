# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
""" Função que calcula e retorna,verdadeiro ou falso, caso o colchão , 
passe ou não pela porta:
int->bool"""
	altura, largura, comprimento = medidas 
    
    if largura > H and comprimento > L:
    	return False
    
    return True