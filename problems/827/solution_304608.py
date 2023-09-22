def qtd_divisores(x):
    '''Funcao que recebe uma entrada int e retorna quantos divisores esse
    numero tem'''
    num = []
    if x<0:
        return 0
    for i in range(x):
        if (i == 0):
            continue
        if (x % i == 0):
                num.append(i)
    num.append(x)
   
    return (len(num))