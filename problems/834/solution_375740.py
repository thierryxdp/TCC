def media_matriz(m):
    '''retorna a media de todos os numeros da matria, com duas casas decimais
    list->float'''
    lista=[]
    for i in range(len(m)):
        for j in range(len(m[i])):
            list.append(lista,m[i][j])
            soma=sum(lista)
            qtd=(i+1)*(j+1)
    return round(soma/qtd,2)