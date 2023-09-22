def primo(x):
    '''funcao que dado um nuemro interio positivo verifica se este numero é primo ou nao e retorna um valor booleano
    int->bool'''
    numP = 0 
    for i in range(1, x + 1):
        if x % i == 0:
            numP += 1
    if numP == 2:
        return True 
    else:
        return False