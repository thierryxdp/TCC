def colchao(medidas,H,L):
	'''funçao que, fornecida uma lista com as medidas
de A, B e C, as dimensoes do colchao, e os tamanhos inteiros 
da altura e largura da porta, (H e L, respectivamente)
retorna se é possivel arrasta-lo atraves de uma porta de tais
dimensoes
list,int,int -> bool'''
	A = medidas[0]
    B = medidas[1]
    C = medidas[2]

    if H>= A and L>=B:
        return True
    if H>=B and L>=A:
        return True
    else:
        return False