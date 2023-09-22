def bolos(A,B,C):
    """Função que retorna a quantidade máxima de bolos que 
    João consegue fazer, dados as medidas A xícaras de
    farinha de trigo, B ovos e C colheres de sopa de leite;
    int, int, int -> int"""
    return round(min(A/2,B/3,C/5))