def colchao(medidas, H, L):
    '''Funcao que dadas as medidas inteiras em centimetros de um colchao em forma de lista, e as medidas em centimetros altura e largura, respectivamente de uma porta, retorna se e possivel passar com o referido colcao na porta;
    entrada: list, int, int
    saida: str'''
	
    dim1 = medidas[0]
    dim2 = medidas[1]
    dim3 = medidas[2]
    
    if ((dim1 >= H or L) and (dim2 and dim3 <= H or L))
    	or ((dim2 >= H or L) and (dim1 and dim3 <= H or L))
        or ((dim3 >= H or L) and (dim1 and dim2 <= H or L))
		return True
    else:
        return False