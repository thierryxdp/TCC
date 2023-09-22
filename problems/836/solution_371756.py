def busca(setor,matriz):
    '''Função que ao receber uma matriz que contém o nome do
    funcionário, registro, setor e telefone do funcionário
    faz uma busca por setor me retornando os dados de todos
    os funcionários daquele mesmo setor.
    str,list ->str'''
    a=0
    i=0
    j=0
    lista=[]
    for linha in matriz:
        for aij in linha:
            if aij==setor:
                a=a+1
            matriz[i]-matriz[i][j].append(lista)
    return lista