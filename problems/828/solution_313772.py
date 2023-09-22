def primo(n):
    """Funcao que verifica se um numero inteiro positivo eh primo ou nao;
    int - > bool"""

    qtdivisores = 0

    for numero in range(1,n+1):
        if n%numero == 0:
            qtdivisores = qtdivisores + 1
            
    if qtdivisores == 2:
        return True
    else:
        return False