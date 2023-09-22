def soma_h(N):
    """Calcula o valor da série harmônica para N termos,
    onde N é a entrada. Retorna o valor da série
    com duas casas decimais.
    int->float"""
    H=0
    for x in range(1,N+1):
        H=H+(1/x)
    return round(H,2)