def soma_h(N):
    """A entrada é um número dado como parâmetro e o retorno
    será um cálculo feito com o mesmo com o resultado de até
    duas casas decimais."""
    #int -> num
    H = 0
    
    for range(1, N+1):
        H + 1 % N
    return round(H, 2)