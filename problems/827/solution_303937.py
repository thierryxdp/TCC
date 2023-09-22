def qtd_divisores(numero):
    """dado um número inteiro, a função retorna a quantidade de divisores
    que esse número possui.
    int-->int
    
    Parâmetros
    numero: numero inteiro. A saída é a quantidade de divisores do numero"""
    contador=0
    for elemento in range(1,numero+1):
        if numero%elemento==0:
            contador=contador+1
    return contador