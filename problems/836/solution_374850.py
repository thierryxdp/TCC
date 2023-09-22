def busca(string,matriz): # matriz com 4 colunas = len(matriz[0]) = 4
    #matriz de strings
    
    lista_infos = []
    
    for funcionario in matriz:
        if string in funcionario:
            lista_funcionarios = []   
            for inf in funcionario:
                if inf != string:
                    list.append(lista_funcionarios,inf)
            list.append(lista_infos,lista_funcionarios)
    return lista_infos