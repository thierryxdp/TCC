def fatorial(numero):
    """Função que recebe um número e calcula o fatorial do mesmo
    
    Parameters:
    numero: numero que terá seu fatorial calculado
    
    Returns:
    Retorna o fatorial do número
    int -> int
    """
    i=0
    fatorial = 1
    num = numero
    while i < numero:
        fatorial = fatorial*num
        num= num-1
        i+=1
    return fatorial