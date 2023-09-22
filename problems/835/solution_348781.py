def melhor_volta(matriz):
    resultado=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            resultado = resultado + [matriz[i][j]]
    if resultado.index(min(resultado))<10:
        corredor=1
    if 10<resultado.index(min(resultado))<20:
        corredor=2
    if 20<resultado.index(min(resultado))<30:
        corredor=3
    if 30<resultado.index(min(resultado))<40:
        corredor=4
    if 40<resultado.index(min(resultado))<50:
        corredor=5
    if 50<resultado.index(min(resultado))<60:
        corredor=6
    return corredor,min(resultado)