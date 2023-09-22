def qtd_divisores(n):
    '''A funca calcula quantos divisores
       o n tem
       int -> int'''
    resposta = []
    n_primos = [1,2,3,4,5,6,7,8,9,11,12,13,17,18,19,23,24,29,31,36,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    for numeros in range(len(n_primos)):
        if n%n_primos[numeros] == 0:
            resposta = [n_primos[numeros]] + resposta
    if n not in n_primos:
        return len(resposta)+1
    if n < 0:
        return 0
    return len(resposta)