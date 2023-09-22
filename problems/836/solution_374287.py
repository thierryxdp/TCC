def busca(setor,matriz):
    '''função que busca os dados de um funcionário
    pelo sertor dado a partir de uma matriz dada com
    as informações
    str,list -> list
    '''
    matriz_dados=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor.lower() == matriz[i][j].lower():
                dados = matriz[i].copy()
                dados.pop(dados.index(dados[j]))
                list.append(matriz_dados,dados)
    return resultado
            
    return corredor, melhor_tempo, volta