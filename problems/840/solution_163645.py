def bolos(a,b,c):
    '''
    Calcula a quantidade de bolos que é possível ser feita dados a quantidade de ingredientes.
    
    Parametros
    ----------
    a : xícaras de farinha de trigo
    b : ovos
    c : colheres de sopa de leite
    '''
     if a<2:
        return 0
    elif b<3:
        return 0
    elif c<5:
        return 0
    else:
        return (a+b+c)//10