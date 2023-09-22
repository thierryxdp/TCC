def soma_h(n):
    '''Entre com um valor para ser retornado a soma de de n+n/n total
    Int/Float -> Float'''

    soma=n

    for y in range(n+1):
        y=y+1
        if y<=n:
            x=n/y
            z=round(x,2)
            soma=soma+z
    return soma