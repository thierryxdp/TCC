#funcao q calcula a quantidade maxima de bolos que se pode fazer dados os igredientes
def bolos (farinha,ovo,leite):
    """calcula a quantidade maxima de bolos dados os igredientes
    float, int, float - int"""
    return min(farinha//2, ovo//3, leite//5)