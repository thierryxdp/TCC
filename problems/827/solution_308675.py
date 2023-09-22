def qtd_divisores(numero):
    ''' esta função verifica a quantos divisores um número qualquer tem
    int --> int'''
    cnt = 0
    for elemento in range(1,numero):
        if numero % elemento == 0:
            cnt += 1
    if numero < 0:
        return cnt
    else:
        return cnt + 1