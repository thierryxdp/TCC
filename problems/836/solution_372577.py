def busca(setor, matriz):
    ''' dada um nome do setor da empresa e a matriz calcula e retorna as informaçoes dos funcionarios daquele setor
str,list-> list '''
    y = []
    for i in matriz:
        for j in i:
            if j == setor:
                list.remove(i, j)
                list.append(y, i)      
    return y