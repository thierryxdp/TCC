def busca(setor,matriz):
    '''função que recebe uma matriz - que fornece funcionarios de uma 
    empresa e seus dados pessoais - e um setor e retorna os dados de
    todos os funcionarios deste setor.
    str,list -> list'''
    #cada linha i corresponde a um funcionário
    #cada coluna j representa os dados do funcionário da linha i
    linhas = len(matriz)
    colunas = len(matriz[0])
    lista_setor = []
    
    for i in range(linhas):
        for j in range(colunas): 
            if setor == matriz[i][2]:
                lista_setor += [matriz[i][0], matriz[i][1], matriz[i][3]],
    return lista_setor