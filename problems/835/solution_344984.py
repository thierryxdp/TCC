def melhor_volta(matriz):
    '''recebe uma matriz 6x10 com as linhas sendo o tempo de cada corredor e as colunas sendo a volta e retorna uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta;lista->tupla'''
    tupla=()
    matriz1=[]
    for m in range(1,7):
        for n in range(1,11):
            matriz1.append(matriz[m][n])
    minimo=min(matriz1)
    for i in range(1,7):
        for j in range(1,11):
            while matriz[i][j]!=minimo:
                tupla=()
            tupla+=(i,j)