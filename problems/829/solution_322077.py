def soma_h(N):
    """
    	Calcula o valor H, dados N termos
    	int->float
    """
    soma=0
    for i in range(1,N):
        soma=round(soma+1/i,2)
    return soma