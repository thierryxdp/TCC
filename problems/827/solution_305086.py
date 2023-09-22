def qtd_divisores(n):
    '''A funca calculla quantos divisores
       o n tem
       int -> int'''
    resposta = []
    n_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    for numeros in range(len(n_primos)):
        if n%n_primos[numeros] == 0:
            resposta = [numeros] + resposta    
    return len(resposta)