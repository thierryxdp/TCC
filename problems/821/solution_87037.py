def fatorial(num):
    '''funcao que dado um numero calcula o seu fatorial
       int -> int '''
    numanterior = num-1
    fatorial = 0
    if(num == 1 or num == 0):
        return 1
    else:
        while(num > 1):
            fatorial = num * numanterior
            num -= 1
            numanterior -= 1
        return fatorial