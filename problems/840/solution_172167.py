def bolos(a, b, c):
    qtd_a=a//2
    qtd_b=b//3
    qtd_c=c//5
    
    if qtd_a <= qtd_b and qtd_a <= qtd_c:
        return qtd_a
    elif qtd_b <= qtd_c:
        return qtd_b
    else:
        return qtd_c