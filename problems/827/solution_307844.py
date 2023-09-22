def qtd_divisores(numero):
    """Função que recebe um número e retorna quantos divisores esse número tem
    entrada: int
    saída: int"""
    i=1
    divisores=0
    while i<numero:
        if numero>0:
            divisores=1
        if numero%i==0:
            divisores=divisores+1
            i=i+1
        else:
            i=i+1
    return divisores