"""Recebe um int e retorna o valor de h de acordo com a expressão h = 1 + 1/2
+ 1/3...+1/n, arrendondado com 2 casas decimais
int -> float"""


def soma_h(n):
    h = 1
    for i in range(2, n+1):
        h = h + 1/i
	return round(h, 2)