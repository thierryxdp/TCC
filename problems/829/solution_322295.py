def soma_h(n):
    '''Retorna o valor H (H = 1 + 1/2 + 1/3 + ... + 1/n)
       com n termos, onde n é o inteiro de entrada;
       int -> float'''
    H=0
    for num in range(1:n+1):
        H+=1/num
    return H