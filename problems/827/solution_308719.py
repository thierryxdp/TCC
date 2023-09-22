def primos(n):
    '''Dado o número 'n', identifica se o mesmo é primo ou não;
int -> str'''
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    
    for i in range(3,10):
        if n%i == 0:
            return False
        
    return False