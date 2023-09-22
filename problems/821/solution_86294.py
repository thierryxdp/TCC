def fatorial(numero):
    resposta = 0
    i=0
    vezes = 0
    while i != numero :
        vezes= vezes + (numero*i)
        if numero > 1:
        resposta = vezes*i
    	
        i=i + 1
    return resposta