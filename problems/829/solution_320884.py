'''Retorna a soma de fracoes 1/N, como 1/1 + 1/2 + 1/3, ate 1/N, com duas casas decimais de precisao'''
#int -> float
def soma_h(N):
    soma = 0
    for index in range(1, N + 1):
        quociente = 1/index
        soma = soma + quociente 
    return round(soma, 2)