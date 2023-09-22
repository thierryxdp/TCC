def qtd_divisores(number):
    """Funcao que calcula e retorna a quantidade de divisores
    de um numero inteiro escolhido.
    Entrada: int;
    Saida: int;
    
    Parameters:
    number: Número para ver seus divisores."""
    divisores = number
    
    if (number >= 0):
        for divisor in range(1,number+1):
            if (number % divisor) != 0:
                divisores -= 1
		return divisores
    else:
        return 0