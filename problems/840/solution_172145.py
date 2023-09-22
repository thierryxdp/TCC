def bolos(a, b, c):
    qtd_a=a//2
    qtd_b=b//3
    qtd_c=c//5
    
    if qtd_a<qtd_b:
        menor=qtd_a
        else qtd_a<qtd_c:
            menor=qtd_a
            else qtd_b<qtd_c:
                menor=qtd_b
                else:
                    menor=qtd_c
    return menor