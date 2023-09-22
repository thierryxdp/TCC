def soma_h(N):
    """Função que calcula a soma de numeros decimais, 
    retornando o valor H dessa soma com duas casas decimais
    entrada: int
    retorno: float"""
    valor= []
    i= 1
    for i in range(1, N+1):
        valor+= 1/i
    valor= round(valor, 2)
    return valor