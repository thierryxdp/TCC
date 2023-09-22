def qtd_divisores(n):
    '''conta quantos divisores um numero tem. int->int'''
    lista=list(range(1,n+1))
    soma=0
    for i in lista:
        if n%lista[i]==0:
            soma=soma+1
    return soma