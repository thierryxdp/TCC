def colchao(lista,x,y):
    '''dada uma lista e dois numeros como parâmetros, a função retorna true se o colchão passa pelas portas de dimensões x,y e false se não. A lista possui as dimensões do colchão.
    list,int,int->booleano
    '''
    if lista[1]>=x: 
        return False
    elif lista[2]>=y:
        return False
    else:
        return True