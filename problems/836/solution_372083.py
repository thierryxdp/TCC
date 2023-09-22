def busca (string,matriz):
    """funcao que recebe uma string e uma matriz que contem os dados dos funcionarios de uma empresa e dado um setor da empresa, retorna uma lista com os dados dos funcionarios daquele setor;
       str,list->lista"""
    lista_busca=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==string:
                lista_busca=lista_busca+[matriz[i]]
            else:
                lista_busca=lista_busca
    return lista_busca