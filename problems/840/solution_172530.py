def bolos(farinha,ovos,leite):
    '''dados os ingredientes (a,b,c) retorna um numeor inteiro de bolos'''
    a=farinha//2
    b=ovos//3
    c=leite//5
    return min(a,b,c)