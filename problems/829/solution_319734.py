def soma_h(n):
    
#Retorna a soma de frações de 1 até 1/n, dado um número inteiro n

    soma = 0

    for i in range(2, n+1):
        soma += 1/i

    return round(soma+1, 2)