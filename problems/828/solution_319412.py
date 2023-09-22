def primo(x):
    '''função que recebe um número e diz se é primo ou não
    entrada da função: int
    saída da função: int '''
	for i in range(1,x//2+1):
        if x % i == 0:
            primo.append(i)
    if len(primo) <= 2:
        return True
    else:
        return False