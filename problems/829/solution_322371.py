def soma_h(n):
    """Função que calcula a soma de 1+1/2+1/3+...+1/n"""
    """Parâmetros de entrada: int"""
    """Parâmetros de saída:float"""
    acumulador=0
    contador=1
    while contador<n:
        acumulador+=(1/contador)
    contador+=1
    return acumulador