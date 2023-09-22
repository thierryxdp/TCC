def primo(n) :
    '''
    O método foi implementado observando que todos os primos têm a forma 6k ± 1, com exceção de 2 e 3 que foram tratados a parte
  	Retorna um valor boleano
  	'''
    if (n <= 1):
        return False
    elif (n <= 3) : 
        return True

    elif (n % 2 == 0 or n % 3 == 0) : 
        return False

    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6

    return True