def colchao(medidas,H,L):
    """Retorna verdadeiro caso as medidas do colchão passem pela porta e falso caso o colchão seja maior que a porta, ou seja, não passe por ela;
    list, int, int -> bool"""
    h_cama = medidas[1]
    l_cama = medidas[0]
    if h_cama <= H:
        if l_cama <= L:
            return True
    else:
        return False