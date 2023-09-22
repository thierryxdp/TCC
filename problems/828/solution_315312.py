def primo(num):
    '''
    	Dado um número inteiro positivo, verifica se este número é primo ou não.
        int -> bool
    '''
    x = True
    for i in range(2,num):
        if num%i==0:
            x = False
            break
    return x