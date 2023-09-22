def colchao(medidas,H,L):
    '''retorna resposta se o colchao ira passar ou nao pela porta
    list,int,int -> bool'''
    medida1 = medidas[0]
    medida2 = medidas[1]
    medida3 = medidas[2]
    
    if H >= medida1:
        if L >= medida2 or L >= medida3:
            return True
    elif H >= media2:
        if L >= medida1 or L >= medida3
        	return True
    elif H >= medida3:
        if L >= medida1 or L >= medida2:
            return True
    return False