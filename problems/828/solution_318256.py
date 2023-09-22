def primo(n):
    '''função em que dado um número inteiro positivo, verifique se este 
    número é primo ou não; int -> bool'''
    num = 0
    for num in range(1, n +1):
        if n % num ==0:
            num += 1
    if num == 2:
        return True
    else:
        return False