def soma_h(n):
    """ Retorna o valor da soma da função H até n com no máximo duas casas decimais; int -> float """
    somatoria=0
    for i in range(1,n+1):
        somatoria=somatoria+1/i;
    return round(somatoria,2);