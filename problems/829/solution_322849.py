def soma_h(termos):
    """
    	Função que calcula o valor de H com o número de 
        termos dado na entrada.
        int -> int
    """
    H = 1
    for x in range(2,termos):
        valor = 1/x
        H = H + valor
    return round(H,2)