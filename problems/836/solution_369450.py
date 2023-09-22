def busca(setor,matriz):
    '''Função que tenha como entrada uma matriz e faça 
    	uma busca por setor retornando os dados de quem
        trabalha no setor. list-->list.'''
    lista =[]
    for x in matriz:
        if x[2]==setor:
            x.remove(setor)
            list.append(setor,x)
    return lista