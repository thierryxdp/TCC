def primo(n):
    
    """
    int--->bool
    Se cria uma variavel com o valor n+2//2. Esse valor é por conta da 
    dica 2 no enunciado, sendo essa variavel x o maior divisor possivel
    de um numero(caso seja divisivel por 2, o valor é tambem divisivel
    pela sua metade).Assim, é criada uma outra variavel que vai do range
    2 até o x, onde caso o numero dado na entrada seja divisivel a algum
    desses valores, retorne falso para a condicao de primo.
    """
    x=(n+2)//2
    
    for i in range(2,x):
        
        if n%i==0:
            return False
        
    else:
        return True