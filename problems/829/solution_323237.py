def soma_h(N):
    """A entrada é um número dado como parâmetro e o retorno
    será um cálculo feito com o mesmo com o resultado de até
    duas casas decimais."""
    #int -> num
    
    listaN = [1]
    H = 0
    
    for i in range(2, N + 1):
        listaN.append((i)** -1))
        H = H + 1/i
    total  = sum(listaN)
    return round(i, 2)