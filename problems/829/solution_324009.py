def soma_h(a):
    """ 
    funcao que retorna o valor de H com N termos 
    int, int -> int
    """
    i=0.0
    for caractere in range(1,a+1):
        i+=1/caractere 
    return round(i,2)