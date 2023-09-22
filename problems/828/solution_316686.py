def primo(n):
    '''função que dado um número inteiro positivo, verifica se esse número é primo ou não; int -> bool'''
    div=0
    for d in range(2,n):
        if n%d==0:
            div+=1
        else:
            div+=0
    if div==0:
        b=True
    else:
        b=False
    return b