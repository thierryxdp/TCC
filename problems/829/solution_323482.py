def soma_h(N):
    '''Função que recebe N termos inteiros, calcula a soma das frações
    e retorna o valor H com esses N termos.
    int -> float
    '''
    soma = [1]
    for num in range(2,N+1):
        soma.append((num)**-1)

    total = sum(soma)

    return round(total,2)