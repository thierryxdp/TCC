def qtd_divisores(numero):
    """Funcao que conte quantos divisores um numero tem;int->int"""
    soma=0
    lista=list(range(1,numero+1))
    for i in lista:
        if numero%i==0:
            soma=soma+1
    return soma