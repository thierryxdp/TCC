#Função que calcule a quantidade maxima de bolos que pode ser feito dados os ingredientes
def bolos (farinha,ovo,leite):
    '''calcula a quantidade maxima de bolos dados os igredientes
    float, int, float - int'''
    return min(farinha//2, ovo//3, leite//5)