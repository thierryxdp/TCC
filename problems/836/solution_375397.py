def busca(setor,dados):
    '''funçao que,dada uma matriz com os dados dos funcionarios de uma empresa e o setor
    desejado, retorna os dados dos funcionarios desse setor;
    str,list(list(str))-->list(list(str))'''
    info=[]
    for i in range(len(dados)):
        if dados[i][2]==setor:
            info = info+[[dados[i][0]]+[dados[i][1]]+[dados[i][3]]]
    return info