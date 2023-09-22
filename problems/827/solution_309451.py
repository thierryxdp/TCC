def qtd_divisores(num):
    '''
    funcao utilizada para contar e retornar
    quantos divisores um numero tem
    int->int
    '''
    res=0
    for div in range((1),num+1):
        if num%div==0:
            res+=1
    return res