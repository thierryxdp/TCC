def primo(n):
    '''
    Esta função recebe um número inteiro e retorna um valor booleano indicando se o número fornecido for primo ou não.
    True será retornado caso o número for primo, False caso o contrário.
    
    Parametros
    ----------
    n (int) : númeor inteiro
    '''
    return [i for i in range(1, n+1) if n%i==0] == [1, n]