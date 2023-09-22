def primo(n):
    """Recebe um número inteiro positivo e retorna se esse
       numero é primo ou não
       parâmetro de entrada:int
       parâmetro de saída:bool"""
    n=1
    mult=0
    for count in range(2,n):
        if (n%count==0):
            mult+=1
            return("Multiplo de ",count)
    if (mult==0):
        return 'True'
    else:
        return 'False'