def colchao (medidas,H,L):
    """Recebe as medidas A, B e C do colchão, ordenadas da menor medida para a maior, junto com  a altura H e o
comprimento L da porta. Tendo esses dados de parametro, a função responde True se o colchão passar pela porta e False se não;
int, int, int, int, int -> bool"""
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if C>H and C>L and B>H and B<L:
     return False
    else:
     return True