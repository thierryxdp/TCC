def busca(setor,matriz):
    ''' Função que recebe uma matriz nx4 referente aos dados de funcionários
    de uma empresa, uma strig referente ao nome de um setor da empresa, e retorna
    os dados de todos os funcionários que pertenem aquele setor
    str,list -> list '''

    Por_Setor = []

    for linha in matriz:

            if setor == linha[2]:
    			list.remove(linha,linha[2])
                Por_Setor.append(linha) 
    return Por_Setor