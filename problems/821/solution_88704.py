def soma_fatorial(n: int) -> int:
    """ recebe um número inteiro 'n' e calcula a soma dos fatoriais
    dos números inteiros de 1 a 'n' """
    soma = 1
    fatoriais = 0
    
    
    for numero in list(range(1, n+1)):
        soma *= numero
        fatoriais += soma
        
    return fatoriais