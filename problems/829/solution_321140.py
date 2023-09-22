def soma_h(n):
    """Funcao calcula e retorna o valor de H com N termos em que N e um inteiro;
    int->float"""
    soma=0
    for i in range(1,n+1):
        h=(1/i)
        soma=soma+h
    return round(soma,2)