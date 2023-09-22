def qtd_divisores(n):
    '''Funcao que calcula a quantidade de divisores do numero de 
    entrada; int->int'''
    quantidade=0
    for numero in range(1,n+1):
        if n%numero==0:
            quantidade=quantidade+1
    return quantidade
def primo(n):
        quantidade=0
    for numero in range(1,n+1):
        if n%numero==0:
            quantidade=quantidade+1
    if quantidade>=2:
        return false
    else:
        return true