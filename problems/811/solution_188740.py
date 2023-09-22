'''A função abaixo determina se um objeto com determinadas medidas consegue passar
por um determinado espaço de altura H e largura L:
	list, int, int -- > bool

OBS: a lista das medidas deve estar ordenada da menor para a maior.
'''

def colchao(medidas,H,L):
    A = medidas[0]  #altura colchão
    B = medidas[1]  #largura colchão
    C = medidas[2]  #comprimento colchão
    if max(H,L) >= C and min(H,L) >= A:
        return True
    if max(H,L) >= B and min(H,L) >= A:
        return True
    if C > max(H,L):
        if max(H,L) >= B and min(H,L) >= A:
            return True
        else:
            return False    	
    if A > min(H,L):
        return False