def soma_h(n):
    'calcula o valor de H, int --> float'
    soma =0
    for i in range(1,n+1):
        soma+= 1.0/i
    return soma