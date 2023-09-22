def soma_h(n):
    '''dado um número n, retorna a soma das frações do tipo 1/2+1/3+1/4+...+1/n com duas casas decimais de precisão;
    int --> float'''
    soma=0
    for num in range(1,n+1):
        soma=soma+(1/num)
    return round(soma,2)