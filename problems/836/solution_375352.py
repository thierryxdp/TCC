def busca(dados,setor):
    '''funçao que, dada uma matriz contendo os dados dos funcionarios
    e o setor da empresa desejado, retorna os dados dos funcionarios desse setor;
    list(list(str)),str-->list(list(str))'''
    acumulador=[]
    for i in range(len(dados)):
        for j in range(len(dados[i])):
            if dados[i][j]==setor:
                list.append(acumulador,dados[i][j])
        return acumulador