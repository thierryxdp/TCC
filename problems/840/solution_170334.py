import math
def bolos(a,b,c):
	"""funçao que retorna a quantidade de bolos que João pode fazer,
    de acordo com a quantidade de ingredientes necessários (2 xícaras de farinha
    de trigo, três ovos e 5 colheres de sopa de leite), sendo:
    a= xícaras de farinha de trigo
    b= ovos
    c= colheres de sopa de leite
    int,int,int->int"""
    return math.floor(min((a/2),(b/3),(c/5)))