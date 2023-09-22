def soma_h(n):
    """Recebe um valor inteiro "n" como entrada, calcula e retorna o valor de H com n termos com precisão de 2 casas decimais;int->float"""
    soma=0
    for val in range(1,n+1):
        inverso=1/val
        soma=soma+inverso
    return soma