import math
def primo(num):
    '''calcula uma função que dado um numero inteiro positivo, 
    retorna se é primo ou não;
    int-->bool.'''
    if num == 2:
        return True
    if num %2 == 0 or num <=1:
        return False
    raiz = int(math.sqrt(num)) + 1
    for i in range(3,raiz,2):
        if num % i == 0:
            return False
    return True