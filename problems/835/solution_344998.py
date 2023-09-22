def melhor_volta(matriz):
    '''recebe uma matriz 6x10 com as linhas sendo o tempo de cada corredor e as colunas sendo a volta e retorna uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta;lista->tupla'''
    matriz1=[]
    quem=()
    tempo=()
    volta=()
    for m in range(0,6):
        for n in range(0,10):
            z=matriz[m][n]
            matriz1.append(z)
    i=0
    while i<len(matriz):
        i+=1
    quem+=(i+1,)
    j=0
    while j<len(matriz[0]):
        j+=1
    volta+=(j+1,)
    minimo=min(matriz1)
    tempo+=(minimo,)
    return quem+tempo+volta