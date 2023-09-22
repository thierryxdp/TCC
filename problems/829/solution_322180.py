#
#
#
#
def soma_h(n):
    soma=0
    i=1
    while i<=n:
        h=1/i
        soma=soma+h
        i=i+1
    return round(soma,2)