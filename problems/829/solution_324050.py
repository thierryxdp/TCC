def soma_h(n):
    """Função que, dado n, calcula o somatório de 1/(n+1)
    assinatura: int --> float"""
    soma=0
    n2 = 1
    cont = 0
    while(cont!=n):
        soma += (1/n2)
        n2+=1
        cont+=1
    return round(soma,2)