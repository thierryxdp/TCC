def primo(n):
    """Recebe um número inteiro positivo e retorna se esse
       numero é primo ou não
       parâmetro de entrada:int
       parâmetro de saída:bool"""
 
    mult=0
    for count in range(2,n):
        if (n%count==0):
            mult+=1
            
    if (mult==0):
        return 'True'
    else:
        return 'False'