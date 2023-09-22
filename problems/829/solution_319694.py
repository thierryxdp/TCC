def soma_h(numero):
    """Função que dado um numero de entrada faz um somatorio das divisoes de um por um ate o numero dado e no final retorna o resultado da soma
    int -> float"""
    H=0
    s=1
    for i in range(1,numero+1):
        H=H+(1/s)
        s=s+1
    return round(H, 2)