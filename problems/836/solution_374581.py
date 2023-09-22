def busca (setor,matriz):
    '''função que dado o nome do setor e a matriz com os
    dados dos funcionários, retorna os dados dos funcionários
    daquele setor
    str,list -> list'''
    
    funcionarios= []
    
    for i in range(len(matriz)):
        for j in matriz[i]:
            if setor == j:
                funcionarios += [matriz[i]]
    for i in range(len(funcionarios)):
        for j in funcionarios [i]:
            if j == setor:
                list.remove (funcionarios[i],setor)
    return funcionarios