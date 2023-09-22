def primo(numero):
    """Função que dado um número inteiro positivo, verifica se ele é 
    primo ou não.
    
    Um número é considerado primo quando possui somente dois divisores:
    1 e ele mesmo.
    
    Parameters:
    numero: Número que será analisado
    
    Returns:
    Retorna True se o número for primo, e False se ele não for.
    int -> bool
    """
    divisores = 0 
    for n in range(1, numero+1):
        if numero%n == 0:
            divisores = divisores +1
        if divisores == 2:
            return True
        else:
            return False