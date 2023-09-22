def primo(n):
    '''Dado um numero inteiro positivo, verifica se este numero e primo ou nao. 
    Retorna um valor booleano
    int -> bool'''
	if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False