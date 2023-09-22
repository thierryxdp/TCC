def soma_h(n):
    """Dado um número n, a função calcula a série (1/1 +1/2...+1/n) e retorna a soma com duas casas decimais;
    int->float"""
    soma=0
    for num in range(1,n+1):
        soma=soma+num**-1
    resultado=round(soma,2)
    return resultado