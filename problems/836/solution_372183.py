def busca (string,matriz):
    """funcao que recebe uma string e uma matriz que contem os dados dos funcionarios de uma empresa e dado um setor da empresa, retorna uma lista com os dados dos funcionarios daquele setor;
       str,list->lista"""
    lista_busca=[]
    for i in range(len(matriz)):
        linha=[]
        for j in range(len(matriz[0])):
            if string!=matriz[i][j] and string in matriz[i]:
                linha.append(matriz[i][j])
        if linha!=[]:
            lista_busca.append(linha)
    return lista_busca