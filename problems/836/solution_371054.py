def busca(setor:str,m:list)->list:
    '''Função que recebe como entrada uma string referente ao setor buscado, e uma matriz com as informações dos funcionários e deve retornar uma lista de funcionários daquele setor.'''
    matriz = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==setor:
                m1=[]
                m1.append(m[i][0])
                m1.append(m[i][1])
                m1.append(m[i][3])
                matriz.append(m1)
    return matriz