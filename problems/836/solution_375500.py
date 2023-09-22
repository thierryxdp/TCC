def busca(setor,matriz):
    '''Dada uma matriz com as informações dos funcionários, realiza uma busca por setor, e retorna os dados de todos os 
    funcionários daquele setor. list(list) -> list''' 
    novo =[]
    for f in matriz:
        if f[2] == setor:
            list.append(novo,[list.remove(f,f[2])])
    return novo