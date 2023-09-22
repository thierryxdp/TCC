def fatorial(numero):
    """Recebe um numero inteiro e calcula o fatorial do mesmo.
    Recebe:int
    Retorna:int"""
    resultado = 1
    count = 1
    
    while count <= numero:
        resultado *=count
        count += 1
        
    return resultado