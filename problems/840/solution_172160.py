def bolos(a, b, c):
    menor=a//2
    qtd_b=b//3
    qtd_c=c//5
    
    if menor > qtd_b:
        menor = qtd_b
    else:
        if menor > qtd_c:
            menor = qtd_c
        else:
            if qtd_b < qtd_c:
                menor=qtd_b
    return menor