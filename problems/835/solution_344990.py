def melhor_volta(matriz):
    '''recebe uma matriz 6x10 com as linhas sendo o tempo de cada corredor e as colunas sendo a volta e retorna uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta;lista->tupla'''
    tupla=()
    matriz1=[]
    for m in range(0,6):
        for n in range(0,10):
            z=matriz[m][n]
            matriz1.append(z)
    minimo=min(matriz1)
    for i in range(0,6):
        for j in range(0,10):
            while matriz[i][j]!=minimo:
                tupla=(minimo)
            tupla+=(i+1,)
            tupla+=(j++1,)
    return tupla