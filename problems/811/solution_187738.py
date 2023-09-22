from math import sqrt
def colchao(medidas,H,L):
	if (medidas[1] > max(H,L)):
        return False
    elif (medidas[0] > min(H,L)):
          return False
    else:
        return True