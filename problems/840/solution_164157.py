def bolos(A,B,C):
    """retorna a quantidade máxima de bolos que João conseguirá fazer dados os números A de xícaras de farinha,B de ovos e C de colheres de sopa de leite"""
    return (min(15*A,10*B,6*C))//30