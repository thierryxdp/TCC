def media_matriz(m):
    """dado uma matriz de inteiros não vazia, retorna a media de 
    todos os numeros da matriz.
    list --> float"""
    soma=0
    if len(m)==0:
        return 0.00
    else:
        numeroLinha=len(m)
        numeroColuna=len(m[0])
        for i in range(len(m)):
            soma=soma+sum(m[i])
        return round(soma/(numeroLinha*numeroColuna),2)