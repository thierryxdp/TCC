def busca(setor, matriz):
    ''' dada a matriz de 4 colunas com as informacoes dos funcionarios de uma empresa na ordem: nome, registro, setor e telefone e o setor desejado, retorna as os dados dos funcionarios daquele setor
    matriz, str -> matriz'''
    result = []
    for line in matriz:
        if (line[2] == setor):
            result.append(line[0:2] + [line[3]])
    
    if(len(result) == 0):
        return "Nenhum registro encontrado"
    
    return result