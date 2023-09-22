def primo(n_int):
    '''Função que retorna se um dado número inteiro positivo (n_int) é primo ou não.
    Entrada: int. Saída: booleano'''
    if n_int==1:
        return False
    for numero in range(2,n_int):
        if n_int%numero==0:
            return False
    return True