def primo(n):
    '''função que recebe um número inteiro positivo n e retorna True se
    n for um número primo ou False se não for.
    entrada:int
    saída:bool'''
    d=[]
    
    for i in range(1,n+1):
        if n%1==0:
            d=d+[i]
            return True
        else:
            return False