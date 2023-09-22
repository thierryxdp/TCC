def qtd_divisores(n):
    '''função que retorna o total de divisores de um numero
    float--> int'''
    vezes=0
    for i in range(1,n+1) :
        if n%i==0:
            vezes+=1
    return vezes