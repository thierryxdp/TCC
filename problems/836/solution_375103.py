def busca(setor, matriz):
    ''' uma função que busca pelo setor, as informações de todos
    funcionários daquele setor.
    matriz, str -> lista'''
    funcao = []
    for a in matriz:
        if setor in a:
            funcao += [[a[0], a[1], a[3]]]
    return funcao