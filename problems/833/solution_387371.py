def conta_numero(numero, matriz):
    '''Função que verifica se existe números em uma matriz'''
    'int, list----->int'
    c=0
    for  i  in  matriz:
        for j in i:
            if j == numero:
                c+=1
            return c