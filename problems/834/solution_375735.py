def media_matriz(m):
    '''retorna a media de todos os numeros da matria, com duas casas decimais
    list->float'''
    for i in range(len(m)):
        for j in range(len(m[i])):
            a=sum(m[i])
            i=i+1
            qtd=i*j
            soma=a
        return round(soma/qtd,2)