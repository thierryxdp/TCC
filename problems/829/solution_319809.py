def soma_h(n):
    """ Retorna o valor da soma da função H até n; int -> float """
    somatoria=0
    for i in range(1,n+1):
        somatoria=somatoria+1/i;
    return somatoria