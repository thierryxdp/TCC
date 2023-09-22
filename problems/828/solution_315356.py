def primo(num):
    '''Uma função dado um inteiro retornar se é primo ou não
    int -> booleano'''
for i in range(1, num + 1):
    if num % i == 0:
        total += 1
        return True
    else: 
        return False