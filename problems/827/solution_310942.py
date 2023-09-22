def qtd_dividores(num):
    '''funcao que conta quantos divisores um numero tem'''
    cont = 0
    for i in range(1,num+1):
        if num % i==0:
            cont+=1
            return cont