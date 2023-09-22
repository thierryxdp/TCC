def busca(setor,matriz):
    ''' Função que recebe uma matriz nx4 referente aos dados de funcionários
    de uma empresa, uma strig referente ao nome de um setor da empresa, e retorna
    os dados de todos os funcionários que pertenem aquele setor
    str,list -> list '''

    Por_Setor = []
    i=0
    for linha in matriz:
        for string in matriz[i]:
            if setor ==  string:
                list.remove(matriz[i],string)
                Por_Setor = Por_Setor + [matriz[i]]
        i=i+1
    return Por_Setor