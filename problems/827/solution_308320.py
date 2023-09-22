def qtd_divisores(n):
    """ Função que recebe como parâmetro de entrada um número
    inteiro e retorna a quantidade de devisores desse número.
    
    int -> int
    """
    
    quantidade_divisores = 0
    for i in range(1, n+1):
        if n%i == 0:
            quantidade_divisores = quantidade_divisores + 1
    return quantidade_divisores