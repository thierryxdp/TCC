def melhor_volta(matriz):
    resultado=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            resultado = resultado + [matriz[i][j]]
    if resultado.index(min(resultado))<10:
        corredor=1
        volta= resultado.index(min(resultado))+1
    if 10<resultado.index(min(resultado))<20:
        corredor=2
        volta= (resultado.index(min(resultado))-9)
        
    if 20<resultado.index(min(resultado))<30:
        corredor=3
        volta= (resultado.index(min(resultado))-19)
        
    if 30<resultado.index(min(resultado))<40:
        corredor=4
        volta= (resultado.index(min(resultado))-29)
    if 40<resultado.index(min(resultado))<50:
        corredor=5
        volta= (resultado.index(min(resultado))-39)
    if 50<resultado.index(min(resultado))<60:
        corredor=6
        volta= (resultado.index(min(resultado))-49)
    return corredor,min(resultado),volta
"""dada uma matriz6x10, retorna a linha do menor numero de toda a matriz
simbolizando o corredor, seguida do valor do menor numero simbolizando o 
tempo,seguida da cordenada da coluna desse numero representando a volta, no formato de uma tupla,list,list->tuple"""