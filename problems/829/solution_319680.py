def soma_h(n):
    '''dada a funcao H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n com n termos, retorna o valor dessa soma para o numero inteiro (n) fornecido
    int -> float'''
    H = 0
    for num in range(1,n+1):
        H = H + 1/num
    return H