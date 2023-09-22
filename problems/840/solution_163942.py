def bolos(A,B,C):
    """essa funcao calcula e retorna a quantidade maxima possivel de bolos 
	a serem feitos dada a quantidade A de farinha de trigo,
 	B de ovos e C de leite disponível para a receita."""
    qtd_farinha = int(A/2)
    qtd_ovos = int(B/3)
    qtd_leite = int(B/5)
    return min(qtd_farinha, qtd_ovos, qtd_leite)