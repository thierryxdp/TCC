def soma_h(n):
    """Função que retorna o valor H com n termos, onde n é inteiro
    entrada: int
    saída: float"""
    soma=0
    for i in range(1,n+1):
        soma=soma+(1/i)
    return round(soma,2)