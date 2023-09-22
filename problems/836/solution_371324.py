def busca(setor,matriz):
    ''' busca os funcionarios que estao em uma matriz a partir do setor deles na empresa, a partir do recebimento do setor deles e dessa matriz e retorna outra matriz0000000000000000000000000000000000000000000000000000000000000000000000000
    str,list(list)->list(list)'''
    funcionarios= []
    linhas= len(matriz)
    for i in range(linhas):
        if matriz[i][2] == setor:
            list.append(funcionarios,matriz[i])
            list.remove(funcionarios,matriz[i][2])
    return funcionarios