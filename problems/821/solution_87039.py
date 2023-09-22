def fatorial(num):
    '''funcao que dado um numero calcula o seu fatorial
       int -> int '''
    fatorial = num
    if(num == 1 or num == 0):
        return 1
    else:
        while(num > 1):
            fatorial = fatorial * (num-1)
            num -= 1
        return fatorial