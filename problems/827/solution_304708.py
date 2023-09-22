def qtd_divisores(x):
    '''funcao que conte quantos divisores um dado numero inteiro tem
    int -> int'''
    qtd = 0
    for i in  range (1,n+1):
        if n%i == 0:
            qtd+=1
    return qtd