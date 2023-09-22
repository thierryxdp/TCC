def tamanho(lista,x,y):
    '''dada uma lista e dois numeros como parâmetros, a função retorna true se o colchão passa pelas portas de dimensões x,y e false se não. A lista possui as dimensões do colchão.
    list,int,int->booleano
    '''
    if lista[2]<=x:
        return True
    elif lista[1]<=x:
        return False
    elif lista[1]<=y:
        return True
    elif lista[2]<=y:
        return True
    else:
        return False