def busca(setor,matriz):
    '''Retorna os dados se todos os funcionarios
    que trabalhem no setor buscado;
    str,list(list) -> list(list)'''
    dados = []
    indice = 0 
    for i in matriz:
        indice = indice + 1
          for j in i:
             if setor in j
                dados.append([matriz[indice][0],matriz[indice][1],matrix[indice][3]])
    
    return dados