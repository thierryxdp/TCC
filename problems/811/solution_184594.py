#Funcao que, dado medias de dimesões de uma porta e um colchão(int), a funcão
#retorna ok
def check(X, Y, h, l): 
	return X <= h and Y <= l;

def colchao(medidas, h, l):
    ok = check(medidas[0], medidas[1], h, l) or check(medidas[1], medidas[2], h, l) or check(medidas[2], medidas[0], h, l) or check(medidas[1], medidas[0], h, l) or check(medidas[2], medidas[1], h, l) or check(medidas[0], medidas[2], h, l)
    return ok