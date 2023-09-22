def colchao(medidas,H,L):
    """Retorna verdadeiro caso as medidas do colchão passem pela porta e falso caso o colchão seja maior que a porta, ou seja, não passe por ela;
    list, int, int -> bool"""
    max_cama = medidas[1]
    min_cama = medidas[0]
    if H >= L:
        max_porta = H
        min_porta = L
    else:
        max_porta = L
        min_porta = H
    if max_cama <= max_porta:
        if min_cama <= min_porta:
            return True
    else:
        return False