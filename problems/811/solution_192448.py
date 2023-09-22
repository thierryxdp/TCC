#Função que calcula se um colchao cabe ou nao#
def colchao(medidas,H,L):
    medidas.sort()
    
    altura = medidas[0]
    largura = medidas[1]
    comprimento = medidas[2]
    if comprimento <= H:
        return True
     if largura <= H:
        return True
     if altura <= L:
        return True
		
		return False