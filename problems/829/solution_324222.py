def soma_h(n):
    """Função que retorna a soma da função (H = 1 + 1/2 + ... + 1/n), onde n é
    o intervalo total da soma. int -> float"""
    numeros = list(range(2,n+1))
    resultado = 1
    for numero in numeros:
        resultado+=1/numero
    return round(resultado,2)