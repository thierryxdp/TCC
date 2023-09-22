ef qtd_divisores(n):
    'conta quantos divisores um numero tem, int --> int'
    div = 2
    If n<0:
        Return 0
    for i in range(2,n):
        if n%i == 0:
            div+=1
    return div