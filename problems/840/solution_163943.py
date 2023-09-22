from math import ceil
def bolos(A,B,C):
    """essa funcao calcula e retorna a quantidade maxima possivel de bolos 
	a serem feitos dada a quantidade A de farinha de trigo,
 	B de ovos e C de leite disponível para a receita."""
    qtd_farinha = ceil(A/2)
    qtd_ovos = ceil(B/3)
    qtd_leite = ceil(B/5)
    return min(qtd_farinha, qtd_ovos, qtd_leite)