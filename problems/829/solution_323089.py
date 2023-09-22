def soma_h(n):
    '''Esta e a funcao que calcula o valor h com
    n termos. onde n é o inteiro e é dado como entrada'''
    a=1
    for num in range(1,n+1):
        a+=1/n
    return a