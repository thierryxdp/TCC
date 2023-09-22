def soma_h(num):
    """recebe um valor inteiro N para numero de termos de
    um valor H, retornando a soma desses termos"""
    c = 0.0
    
    for i in range(1, num+1):
        c+= 1/i
    return round(c,2)