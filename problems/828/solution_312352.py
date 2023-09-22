def qtd_numeros (n):
    'conta quantos divisores um numero tem, int --> int'
    div = 2
    for i in range(2,n):
        if n%i == 0:
            div+=1
    return div

def primo(n):
    if qtd_numeros(n) == 2:
        return True
    else:
        return False