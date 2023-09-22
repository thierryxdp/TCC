def media_matriz(matriz):
    '''dada uma matriz, retorna a media de 
    todos os seus numeros
    entra:lista
    sai:float'''
    entradas=[]
    for i in matriz:
        for k in i:
            entradas.append(k)
    return round(sum(entradas)/len(entradas),2)