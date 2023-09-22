def primo(n):
    """essa função recebe um número qualquer e identifica se ele é ou não um número primo;
    int->bool"""
    for i in range(2,n):
        if n%i==0:
            return False
    return True