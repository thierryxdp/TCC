def soma_h(n):
    """Calcula e retorna H através do parâmetro n de entrada.
    Sendo H, soma de 1 + 1/N
    n --> int
    lista --> lista
    soma
    """
    lista = []
    H = 1
    for i in range(2,n+1):
        lista.append(1/i)
        H = H + (1/i)
    return round(H,2)