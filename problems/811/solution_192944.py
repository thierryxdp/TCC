def colchao(medidas,H,L):
    """Retorna verdadeiro caso as medidas do colchão passem pela porta e falso caso o colchão seja maior que a porta, ou seja, não passe por ela;
    list, int, int -> bool"""
    menor_lado_cama = medidas[1]
    menor_lado_cama = medidas[0]
    if H >= L:
        maior_lado_porta = H
        menor_lado_porta = L
    else:
        maior_lado_porta = L
        menor_lado_porta = H
    if menor_lado_cama <= maior_lado_porta:
        if menor_lado_cama <= menor_lado_porta:
            return True
    else:
        return False