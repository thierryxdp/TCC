def soma_h(n):
    """esta funçao retorna a soma de números 1+1/2+1/3+...+1/n com duas casas decimais
    int->float"""
    soma=0
    for numero in range(n+1):
        if numero==0:
            soma=0
        else:
            soma+=1/numero
    return round(soma,2)