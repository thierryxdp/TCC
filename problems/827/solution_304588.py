def qtd_divisores(numero):
    """Função que dado um número inteiro, retorna a quantidade de 
    divisores que esse número possuí.
    
    Parameters:
    numero: É o número escolhido para encontrar os divisores
    
    Returns:
    Retorna a quantidade de divisores do número passado.
    int -> int
    """ 
    divisor = 0
    for n in range(1,numero+1):
        if numero%n==0:
            divisor = divisor+1
    return divisor