def soma_h(n):
    """Realiza uma operação para a função de h.
    Assinatura: int -> float"""
    contador=0
    h=0
    while contador<=n:
        contador+=1
        h+=1/contador
    return round(h,2)