def qtd_divisores(num):
    '''Função que conta quantos divisores um dado número inteiro tem
    int->int'''
    L=[]
    for i in range(1,num+1):
        if num%i==0:
            list.append(L,i)
    return len(L)