def primo(n):
    '''indica se um número n inteiro positivo é primo ou não.
    int -> bool'''
    
    divisores = []
    
    for numero in range(1, (n//2)+1):
        if n%numero == 0:
            list.append(divisores, numero)
    return len(divisores)==1