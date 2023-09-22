def qtd_divisores(numero):
    """Recebe um número e diz quantos divisores ele possui;
    	int -> int"""
    total=0
    for divisor in range(1,numero+1):
        if numero%divisor==0:
            total=total+1
    return total