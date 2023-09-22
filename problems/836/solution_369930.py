def busca(nome,matriz):
    """Retorna os dados de todos os funcionários dado o setor da empresa.
    string, lista --> lista"""
    
    lista_funcionarios = []
    
    for i in range(len(matriz)):
        if nome in matriz[i]:
            list.append(lista_funcionarios, matriz[i])
            list.remove(lista_funcionarios[i], nome)
    
    
    return lista_funcionarios