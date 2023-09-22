def soma_h(n):
    """ a função retorna a soma uma range entre o primeiro numero 1 e n + 1, que é o valor de h"""
    h = 0
    for i in range(1,n+1):
        h = h + 1/i
    return round(h,2)