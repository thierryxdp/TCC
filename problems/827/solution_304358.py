def qtd_divisores(n):
    '''utilizando a função range para retornar uma lista de 1
    até o número que eu desejo sendo que coloquei n+1 para acrescentaro n
    também porque o ranger para no numero anterior a n''' 
    lista=list(range(1,n+1))
    c=0
    for i in lista:
        if n%i == 0:
            c+=1
    return c