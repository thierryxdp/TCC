def soma_h(N):
    """Dada uma função H=1+(1/2)+(1/3)+(1/4)+...+1/N e dado o número
    inteiro 'N', a função retorna o valor de H com 2 casas decimais;
    int -> float"""
    H = 0

    for x in range(1,N+1):
        equacao = (1/x)
        H = H + equacao
    return round(H,2)