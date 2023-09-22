def soma_h(n):
    soma=0
    for f in range(1,n+1):
        fracao=(1/f)
        soma= soma+fracao
    return round(soma,2)