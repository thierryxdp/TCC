def soma_h(n):
    '''retorna a soma com N termos, onde N é o último divisor da crescente soma de frações
    int -> float'''
    soma = 0
    for i in range(1,n+1):
        soma += 1/i
    return round(soma,2)