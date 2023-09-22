def melhor_volta(matriz):
    '''Função conta e retorna a quantidade de ocorrencia do numero de entrada em uma matriz.
    int, matriz->int'''
    lista=[]
    for i in range (6): #linhas
        for j in range (10): #colunas
            lista.append(matriz[i][j]) #Insere cada elemento em uma lista só
    melhorVolta=min(lista)
    linha1=[0,1,2,3,4,5,6,7,8,9]
    linha2=[10,11,12,13,14,15,16,17,18,19]
    linha3=[20,21,22,23,24,25,26,27,28,29]
    linha4=[30,31,32,33,34,35,36,37,38,39]
    linha5=[40,41,42,43,44,45,46,47,48,49]
    linha6=[50,51,52,53,54,55,56,57,58,59]
    if lista.index(melhorVolta) in linha1:
        corredor=1
    if lista.index(melhorVolta) in linha2:
        corredor=2
    if lista.index(melhorVolta) in linha3:
        corredor=3
    if lista.index(melhorVolta) in linha4: 
        corredor=4
    if lista.index(melhorVolta) in linha5:
        corredor=5
    else:
		corredor=6
    return (corredor,melhorVolta)