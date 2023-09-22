import math
def colchao(medidas,H,L):
    lado1 = medidas[0]
    lado2 = medidas[1]
    lado3 = medidas[2]
    diagonal1c2 = math.sqrt(lado1**2 + lado2**2)
    diagonal1c3 = math.sqrt(lado1**2 + lado3**2)
    diagonal2c3 = math.sqrt(lado2**2 + lado3**2)
    if H >= lado1 or H >= lado2 or H >= lado3 :
        return True
    if L >= lado1 or L >= lado2 or L >= lado3 :
        return True
    else:
        return False