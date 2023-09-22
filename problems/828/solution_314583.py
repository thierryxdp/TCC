def qtd_divisores(n):
    '''retorna a quantidade de divisores de n
    int-->int'''
    qtd=0
    for i in range(1,n+1):
        if n%i==0:
            qtd+=1
    return qtd

def primo(n):
    '''Retorna True se n for primo, False caso contrário
    int-->bool'''
    if qtd_divisores(n)==2:
        return True
    else:
        return False