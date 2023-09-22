def soma_h(n):
    """Retorna o valor H com N termos sendo N a entrada. O resultado possui 2
    casas decimais.
    int->float"""
    sequencia=0
    for c in range(1,n+1):
        H=1/c
        sequencia+=H
    return round(sequencia,2)