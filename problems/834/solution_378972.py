def media_matriz(m):
    ''' função que retorna a média dos números de uma matriz, dada a mesma como parâmetro
    list --> float '''
    soma=0
    if len(m) == 0:
        return 0.00
    else:
        numerolinha = len(m)
        numerocoluna = len(m[0])
        for i in range(len(m)):
            soma = soma+sum(m[i])
        return round(soma/(numerolinha*numerocoluna),2)