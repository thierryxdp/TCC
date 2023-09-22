def soma_h(N):
    """Função repete para cada número de 1 até o N recebido o processo
    de somar (1/número) a H (inicialmente 0). Após conclusão da soma
    pelo último número (que é 1/N), retorna H
    int-> float"""
    H=0
    for divisor in range(1,N+1):
        H+=(1/divisor)
    return round(H,2)