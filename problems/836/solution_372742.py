def busca(setor,matriz):
    '''Função que ao receber uma matriz que contém o nome do
    funcionário, registro, setor e telefone do funcionário
    faz uma busca por setor me retornando os dados de todos
    os funcionários daquele mesmo setor.
    str,list ->str'''
    a=0
    b=0
    quero=[]
    lista=[]
    lista_quero=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            a=a+1
            if matriz[i][j]==setor:
                lista+=matriz[i]                
                lista.append(lista_quero)
                lista_quero.remove('setor')
            else:
                lista_quero
    return lista_quero