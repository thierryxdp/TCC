def qtd_divisores(num):
    '''função responsável por contar o número de divisores de um número,num'''
    x=0
    a=list(range(1,num+1))
    for i in a:
        if num%i==0:
            x=x+1
    return x