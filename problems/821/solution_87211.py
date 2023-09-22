def fatorial(numero):
    """Função que recebe um número e calcula o fatorial do mesmo
    
    Parameters:
    numero: numero que terá seu fatorial calculado
    
    Returns:
    Retorna o fatorial do número
    int -> int
    """
    i=1
    fatorial = 0
    while i < numero:
        fatorial = fatorial + i
    i+=1
        return numero*numero-i