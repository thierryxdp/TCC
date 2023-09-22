def qtd_divisores(n):
    '''
    Calcula a quantidade de divisores que dado número inteiro n possui.
    int -> int

    Parameters:
    n: Parâmetro numérico, do tipo inteiro (int).

    Returns:
    A quantidade de divisores que determinado número n possui.

    O teste do código foi realizado utilizando valores elucidativos inteiros
    positivos e diferentes de zero para o parâmetro, de modo que o resultado
    gerado pelo código seja condizente com o resultado previsto na solução
    manual do problema.
    '''
    i = 0
    divisores = []

    possiveis_divisores = range(1, n+1)
    
    for numero in possiveis_divisores:
        if n%numero == 0:
            list.append(divisores, numero)

    return len(divisores)