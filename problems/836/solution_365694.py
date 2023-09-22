def busca(setor,matriz):
    '''funcao que dado uma matriz com os
    dados de cada funcionario busca e retorna 
    os que trabalham no setor indicado;
    str,list -> list'''
    
    funcionarios = []
    for i in range(len(matriz)):
        if setor == matriz[i][2]:
            list.append(funcionarios,matriz[i][0])
            list.append(funcionarios,matriz[i][1])
            list.append(funcionarios,matriz[i][3])
            todos = [funcionarios]
    return todos