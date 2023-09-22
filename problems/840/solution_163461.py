def bolos(farinha,ovos,leite):
    """Calcula a quantidade máxima de bolos
       que podem ser feitos a partir da receita
       base e dos dados inseridos;
       int,int,int->int"""
    ff=farinha//2
    of=ovos//3
    lf=leite//5
    return min(ff,of,lf)