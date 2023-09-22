def media_matriz(m):
    """ Funcao que recebe uma matriz "m" de entrada e calcula
    a médias dos elementos dessa matriz, retornando o resultado
    dessa operação matemática """
    """ list -> float """
    Somatorio=0
    Total=0
    Media=0
    if m != []:
        for L in range(0,len(m)):
            for C in range(0,len(m[L])):
                Total+=1
                Somatorio+=m[L][C]
                Media= Somatorio/Total
    return round(Media,2)
#Casos de teste:
""" media_matriz([[1,2,3],[2,3,4]])
>>> 2.5
    media_matriz([[10,10],[20,20],[30,30]])
>>> 20
    media_matriz([[45],[50],[62]])
>>> 52.33  """