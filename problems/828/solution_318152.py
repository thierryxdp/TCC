def primo(n):
    '''Dano um numero inteiro positivo n, a função retorna True se
    n for primo e False se n não for primo. int --> bool'''
   
    i=2
   
    while i<n:
        if n%i==0:
            return False
           
        i=i+1
    return True