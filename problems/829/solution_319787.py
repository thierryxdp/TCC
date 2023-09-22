def soma_h(n): #Recebe int
    soma = 0
    for i in range(1,n+1): #Pra cada número inteiro entre 1 e n
        soma = 1/i + soma #Aplicados na fórmula
    soma = round(soma, 2) #Arredonda a soma
    return soma #Retorna int