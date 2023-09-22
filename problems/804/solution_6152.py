def filtra_pares(x):
    """ função que recebe uma tupla com 4 elementos inteiros e retorna dentre esses mesmos, quais são pares
 		entrada: tupla (int,int,int,int,)
    	saida: tupla dos números pares dentre os inteiros
        n1, n2, n3, n4
    """
    resposta = ()
    
    if x[0] % 2 == 0:
    	resposta = resposta + str(x[0])
    if x[1] % 2 == 0:
    	resposta = resposta + str(x[1])
    if x[2] % 2 == 0:
    	resposta = resposta + str(x[2])
    if x[3] % 2 == 0:
    	resposta = resposta + str(x[3])
        return resposta