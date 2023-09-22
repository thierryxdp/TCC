def qtd_divisores(x):
    '''funcao que conta quantos divisores um numero tem. int->int.'''
    l = []
    for numeros in range(1,x+1):
        if x % numeros == 0:
            list.append(l,numeros)
    return len(l)