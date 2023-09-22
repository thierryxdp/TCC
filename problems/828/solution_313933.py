def primo(n):
    '''dado um número inteiro positivo(n), retorna True se o número
    for primo e False se não for; int -> bool'''
    lista = []
    for i in range(1,n+1):
        if n%i == 0:
            lista.append(i)
    if len(lista) <= 2:
        return True
    else:
        return False