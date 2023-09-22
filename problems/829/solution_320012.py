def soma_h(N):
    """Função que calcula a soma de numeros decimais, 
    retornando o valor H dessa soma com duas casas decimais
    entrada: int
    retorno: float"""
    valor= []
    i= 1
    saida=0
    for i in range(1, N+1):
        valor.append(1/i)
    saida=round(sum(valor), 2)
    return saida