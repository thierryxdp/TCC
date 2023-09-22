def busca(setor, matriz):
    ''' uma função que busca pelo setor, as informações de todos  os funcionarios da empresa
    daquele setor.
    matriz, str -> lista'''
    for a in matriz:
        if setor in a:
            funcao +=[a[0], a[1], a[3]]
    return funcao