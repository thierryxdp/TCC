def primo(n):
    '''indica se um número n inteiro positivo é primo ou não.
    int -> bool'''
    
    divisores = []
    
    for numero in range(1, n/2):
        if numero%n == 0:
            list.append(divisores, numero)
    return len(divisores)==1