def primo(n):
    '''
    Verifica se dado número inteiro positivo n é primo ou não.
    int -> bool

    Parameters:
    n: Parâmetro numérico, do tipo inteiro (int).

    Returns:
    Um valor booleano:
      # True: caso o número informado seja primo;
      # False: caso contrário.

    O teste do código foi realizado utilizando valores elucidativos inteiros
    positivos para o parâmetro, de modo que o resultado gerado pelo código seja
    condizente com o resultado previsto na solução manual do problema.
    '''
    i = 0
    divisores = []

    possiveis_divisores = range(1, n+1)
    
    for numero in possiveis_divisores:
        if n%numero == 0:
            list.append(divisores, numero)

    if len(divisores) == 2:
        return True
    else:
        return False