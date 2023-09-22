def primo(n):
    ''' função que verifica se um número inteiro positivo é primo e retorna um valor booleaano;
	int -> bool '''
    if n > 1:
        for x in range(2, n):
            if (n % x) == 0:
                return False
        else:
            return True
 
    else:
        return False