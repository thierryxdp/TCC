def soma_h(n):
    '''Função que calcular e retornar o valor H com N termos, onde N é inteiro
e é dado como entrada. int -> float'''
    soma = 0
    for h in range(n):
        soma += (1/(h+1))
    return round(soma,2)