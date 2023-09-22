def soma_h(n):
    '''Função que retorna o valor de H com n termos, onde n é um número inteiro
    int -> float'''
    h=0
    for i in range(1,n+1):
        h+=1/i
    return round(h,2)