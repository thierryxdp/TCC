def busca(setor,matriz):
    '''Retorna os dados se todos os funcionarios
    que trabalhem no setor buscado;
    str,list(list) -> list(list)'''
    dados = []
    indice = -1
    for i in matriz:
        indice = indice + 1 
        for j in i:
            if setor in j:#Cria uma matriz com os dados buscados
               dados.append([matriz[indice][0],matriz[indice][1],matriz[indice][3]])