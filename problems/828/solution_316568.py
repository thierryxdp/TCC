def primo(n):
    '''função que recebe um número inteiro positivo n e retorna True se
    n for um número primo ou False se não for.
    entrada:int
    saída:bool'''
    d=[]
    
    for i in range(1,round(n**0.5)+1):
        if n%i==0:
            d=d+[i]
  
    if len(d)==1:
            return True
    else:
            return False