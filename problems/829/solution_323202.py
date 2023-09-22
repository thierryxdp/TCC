def soma_h(n:int):
    "Calcula e retorna H com N termos"
    soma = 0
    for c in range(1, n + 1):
        inverso = (1/c)
        soma += inverso
    return round(soma, 2)