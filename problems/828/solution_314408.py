def primo (n):
    """Funcao que dado um numero inteiro positivo, verifique se este numero é primo ou não. Retorne um valor booleano.
    int -> bool"""
    divisivel=[]
    for x in range(1, n+1):
        if n % x ==0:
            list.append(divisivel, x)
    return len(divisivel) == 2