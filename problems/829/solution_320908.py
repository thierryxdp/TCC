def soma_h(n):
    H = 0
    for i in range(1, n+1):
        H += 1/i 
    return round(H, 2)

# Primeiro temos um loop que percorre todos os números de 1 até H,
# dentro desse loop, faz-se a divisão de 1 por i (que recebe os valores de 1 até H)
# e soma-se à variável H, com isso, obtem-se o somatório desejado.