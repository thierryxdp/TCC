def primo(n):
    """função que calcula e retorna se um número é primo ou não, através do valor de entrada n;
    Entrada: int
    Saída: bool"""
    x = range(2,n)
    
    for numero in x:
        if n % numero == 0:
            return False
    return True