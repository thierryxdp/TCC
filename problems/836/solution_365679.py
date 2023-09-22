def busca(setor,matriz):
    '''funcao que dado uma matriz com os
    dados de cada funcionario busca e retorna 
    os que trabalham no setor indicado;
    str,list -> list'''
    
    funcionarios = []
    for i in range(len(matriz)):
        if setor == matriz[i][2]:
            m = matriz[i].remove(matriz[i][3])
            list.append(funcionarios,m)
    return funcionarios