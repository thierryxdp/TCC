def soma_h(N):
    """Funcao que, dado o numero dos N termos de entrada, retorna o resultado do valor H,
    sendo que o resultado é dado com apenas duas casas decimais;
    int -> float"""
    soma_dos_n_valores=(1)
    for denominador in range(2,N+1):
        soma_dos_n_valores+=(1/denominador)
    return round(soma_dos_n_valores,2)