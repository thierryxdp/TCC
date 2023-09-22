def busca(setor, cadastro):
    '''
        recebe uma string com o nome de um setor cadastrado com dados de
        funcionarios e recebe uma lista, matriz, com os dados cadastrados
        de funcionarios e retorna uma lista, submatriz com funcionarios e
        dados desses funcionarios do setor dado
        entrada: string, lista
        saida: lista
    '''
    resultado = []
    for i in range(len(cadastro)):
        if setor in cadastro[i]:
            resultado = resultado + [[cadastro[i][0], cadastro[1][1], cadastro[i][3]]] 
    return resultado