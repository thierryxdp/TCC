def melhor_volta(matriz):
    resultado=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            resultado = resultado + [matriz[i][j]]
    if resultado.index(min(resultado))<10:
        corredor=1
    if resultado.index(min(resultado))<20:
        corredor=2
    if resultado.index(min(resultado))<30:
        corredor=3
    if resultado.index(min(resultado))<40:
        corredor=4
    if resultado.index(min(resultado))<50:
        corredor=5
    if resultado.index(min(resultado))<60:
        corredor=6
    return corredor