def soma_h(n):
    "Calcula e retorna o numero baseado na funcao da questao"
    "int -> float"
    H = 0
    for x in range(n):
        H = H + 1/(x+1)
    return round(H,2)