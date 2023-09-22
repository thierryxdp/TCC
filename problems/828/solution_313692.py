def primo(n):
    """Funcao que dado como parametro de entrada um numero
    inteiro positivo n, verifica se este numero e primo ou 
    nao. A funcao retorna o valor booleno True, caso o
    numero seja primo e False, caso nao seja;
    int->bool"""
    
    Quantidade=0
    
    for divisor in range(1,n+1):
        if n%divisor==0:
            Quantidade=Quantidade+1
            
    if Quantidade==2:
        return True
    if Quantidade!=2:
        return False