def qtd_divisores(n):
    	# Função que dado um número, retorna o número total de divisores
        # int > int
        qtd = 0
        listaNum = list(range(1, n + 1))
        for i in range(len(listaNum)):
                if n % listaNum[i] == 0:
                        qtd = qtd + 1
        return qtd