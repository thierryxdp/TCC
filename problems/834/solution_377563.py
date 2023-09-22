def media_matriz(m):
    '''
    Funcao que tem como entrada uma matriz nao vazia e 
    retorna a media de todos os numeros dessa matriz.
        Parametros:
            entrada:
                matriz : list
            saida:
                float
    '''
    a = []
    b = []
    for i in range(len(m)):
        c = len(m[i])
        d = sum(m[i])
        a.append(c)
        b.append(d)
    return round(sum(b)/sum(a),2)