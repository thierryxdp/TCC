def primo(x):
    '''função que recebe um número e conta quantos divisores esse mesmo número tem
    entrada da função: int
    saída da função: int '''
    if x <= 0:
        return 0
    primo = [x]
    for i in range(1,x//2+1):
        if x % i == 0:
            primo.append(i)
    if len(primo) <= 2:
        return True
    else:
        return False