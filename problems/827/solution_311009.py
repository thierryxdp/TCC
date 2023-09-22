def qtd_divisores(num):
    '''funcao que conta a quantidade de divisores de um numero'''
 
    seq=list(range(1,num+1))
    divisores=[]
    for i in seq:
        if num%i==0:
            divisores.append(i)
    return len(divisores)