def soma_h(n):
    """Função que dado um número inteiro(n) retorne a somas de n na série h.
    int -> float"""
    total = 0
    indice = 0
    for num in range(n):
        indice = indice + 1
        total = total + total + (1/indice)


    return round(resultado,2)