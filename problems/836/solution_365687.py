def busca(setor,matriz):
    '''funcao que dado uma matriz com os
    dados de cada funcionario busca e retorna 
    os que trabalham no setor indicado;
    str,list -> list'''
    
    funcionarios = []
    for i in range(len(matriz)):
        if setor == matriz[i][2]:
            nova_matriiz = matriz[:2] + matriz[3]
            list.append(funcionarios,nova_matriz[i])
    return funcionarios