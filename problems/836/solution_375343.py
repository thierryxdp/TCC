def busca (setor, matriz):
    '''Função que recebe uma amtriz e o setor busca e nos retorna todos os dados de quem está em tal setor'''
    
    i = 0
    adicionar = []
    
    while i < len(matriz):
        if setor in matriz[i]:
            nome = matriz[i][0]
            registro = matriz[i][1]
            telefone = matriz[i][3]
            adicionar += [[nome,registro,telefone],]
        i += 1
    return adicionar