def soma_h(N):
    '''calcula a soma da sequencia 1/N, sendo N igual a um numero inteiro positivo, de 
    N=1 ate o N dado
    int-->float'''
    soma=0
    for i in range(1,N+1):
        soma+=1/i
    return round(soma,2)