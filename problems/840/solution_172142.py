def bolos(a, b, c):
    menor=round(a/2)
    qtd_b=round(b/3)
    qtd_c=round(c/5)
    if menor > qtd_b:
        menor = qtd_b
    elif menor > qtd_c:
            menor = qtd_c
    return menor