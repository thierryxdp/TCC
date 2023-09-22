def busca(m, setor):
    '''função retorna os dados das pessoas de determinado setor
    list,str--->list'''
    encontra = []
    for i in range(len(m)):
        if str(setor) in m[i]:
            ficha=[]
            for j in range(len(m[0])):
                if  m[i][j] != str(setor):
                    list.append(ficha,m[i][j])
            list.append(encontra, ficha)
    return encontra