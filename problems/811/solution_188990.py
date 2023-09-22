def colchao(medidas,H,L):
    '''retorna true se o colchao de medidas AxBxC (que estao dentro da lista medidas,
    	em ordem crescente) entra pela porta de altura H e largura L
        list,int,int->bool'''
    
    return medidas[0]<=L and medidas[1]<=H