def primo(n):
    """Essa função dado um número informa se o mesmo é primo ou não.
    Como entrada temos um número inteiro e como saída temos a informaçã0
    booleana se ele é ou não um número primo;
    int->bool"""
    for i in range(2,n//2+1):
        if (n%i)==0:
            return False
    else:
        return True