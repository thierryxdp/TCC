def bolos (a,b,c):
		'''Função que calcula número máximo de bolos possíveis dado medidas de xícaras de farinha de trigo (a), ovos (b) e colheres de sopa de leite (c) '''
		import math
        return math.floor (min ((a/2),(b/3),(c/5)))