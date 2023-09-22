def bolos (farinha,ovo,leite):
    '''calcula a quantidade maxima de bolos dados os igredientes;
    int, int, int - int'''
    return min(farinha//2, ovo//3, leite//5)