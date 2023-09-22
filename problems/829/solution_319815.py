def soma_h(n):
    '''
    Calcula a soma de uma série H até certo termo n.
    int -> float

    Parameters:
    n: Parâmetro numérico, do tipo inteiro (int).

    Returns:
    A soma dos n termos de H.

    O teste do código foi realizado utilizando valores elucidativos inteiros
    positivos e diferentes de zero para o parâmetro, de modo que o resultado
    gerado pelo código seja condizente com o resultado previsto na solução
    manual do problema.
    '''
    
    if type(n) != int or n <= 0:
        return ("O termo 'n' deve ser do tipo inteiro e maior que zero. \
Tente novamente!")
    
    H = 1
    lista_numeros = range(2, n + 1)
    
    for numero in lista_numeros:
        H += (1 / numero)

    H = round(H, 2)
    return H