def busca(setor,matriz):
    ''' busca os funcionarios que estao em uma matriz a partir do setor deles na empresa, a partir do recebimento do setor deles e dessa matriz e retorna outra matriz0000000000000000000000000000000000000000000000000000000000000000000000000
    str,list(list)->list(list)'''
    funcionarios= []
    linhas= len(matriz)
    vezes_que_aparece = 0
    for i in range(linhas):
        if matriz[i][2] == setor:
            list.append(funcionarios,matriz[i])
            del funcionarios[vezes_que_aparece][2] 
            vezes_que_aparece = vezes_que_aparece + 1
    return funcionarios