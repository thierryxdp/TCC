def busca(setor,dados):
    '''funcao que, dada um matriz contendo os dados dos funcionarios
    de uma empresa e um determinado setor da empresa, realiza uma busca
    na matriz e retorna as informações dos funcionarios pertencentes no setor.
    matriz(str) -> lista'''
    lista_dados=[]
    for i in range(len(dados)):
        if dados[i][2] == setor:
            info = [dados[i][0],dados[i][1],dados[i][3]]
            list.append(lista_dados,info)
    return lista_dados