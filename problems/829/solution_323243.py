def soma_h(N:int)->bool:
    """Calcula e retorna o valor H com N termos onde N é inteiro e dado como entrada."""
    sequencia=list(range(N,0,-1))
    H=0
    for i in sequencia:
        H=H+1/i
    return round(H,2)