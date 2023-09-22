def soma_h(N):
    """
    Essa função retorna o valor 'H' com 'N' termos, 
    onde N  ́e inteiro e  ́e dado como entrada.
    
    H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
    
    Entrada: int
    Saida: int
    """
    soma = 0
    for x in range(N):
        if N >= 1:
            soma = soma + (1/(x+1))
    return round(soma,2)