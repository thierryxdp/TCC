def soma_h(N):
    """dado um número inteiro N, a função calcula a soma:
    H=1+1/2+1/3+...+1/N. A função retorna o valor H dessa soma,
    com precisão de duas casas decimais.
    int-->float
    
    Parâmetros
    N: número inteiro que será o denominador da última parcela da soma
    H: acumulador da soma. Será arredondado e utilizado para o retorno da função"""
    H=0
    for elemento in range(1,N+1):
        H=H+1/elemento
    return round(H,2)