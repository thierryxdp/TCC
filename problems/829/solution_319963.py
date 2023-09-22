def soma_h(N):
    """Funcao que calcula e retorna o valor H com N termos onde N é interio e dado como entrada;int->float"""
    soma=0
    lista=list(range(1,N+1))
    for i in lista:
        x=1/i
        soma=soma+x
    return round(soma,2)