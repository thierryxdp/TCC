def media_matriz(m:list) -> float:
    """"função que retorna a media de todos os numeros da matriz com duas casas decimais de precisão
    
    parametros:
    list -> float
    
    exemplos:
    media_matriz([[1],[3]])==2
    media_matriz([[2,4,6],[1,3,2]])==3
    media_matriz([[1],[1]])==1"""
    
    acumulador=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            acumulador+=m[i][j]
    return round(acumulador/(len(m)*len(m[0])),2)