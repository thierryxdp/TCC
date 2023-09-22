def colchao(medidas,H,L):
    """Retorna verdadeiro caso as medidas do colchão passem pela porta e falso caso o colchão seja maior que a porta, ou seja, não passe por ela;
    list, int, int -> bool"""
    A = medidas[1]
    B = medidas[0]
    if H >= L:
        maior_porta = H
        menor_porta = L
    else:
        maior_porta = L
        menor_porta = H
    if B <= maior_porta:
        if A <= menor_porta:
            return True
    else:
        return False