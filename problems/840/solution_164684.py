def receitabolo(a,b,c):
		'''Função que calcula número máximo de bolos possíveis dado medidas de xícaras de farinha de trigo (a), ovos (b) e colheres de sopa de leite (c) sendo todas as medidas maiores ou iguais a 1 ou menores ou iguais a 100'''
		import math
        return math.floor((a+b+c)/10)