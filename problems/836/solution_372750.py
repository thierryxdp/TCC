def busca(setor,matriz):
    '''Função que ao receber uma matriz que contém o nome do
    funcionário, registro, setor e telefone do funcionário
    faz uma busca por setor me retornando os dados de todos
    os funcionários daquele mesmo setor.
    str,list ->str'''
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==setor:
                lista=lista+[matriz[i]]
    i=0
    while i < len(lista):
        lista[i].remove(setor)
        i+=1
    return lista