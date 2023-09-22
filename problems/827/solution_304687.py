def qtd_divisores(num):
    """Funcao que informa quantos divisores um numero tem.
    	Sendo "num" a entrada de um numero inteiro."""
    quantidade = 0
    for i in range(1, num//2+1):
        if num % i == 0: 
            quantidade +=1
    return quantidade