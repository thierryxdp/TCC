def media_matriz(matriz):
    '''retorna a media de todos os numero presentes dentro da matriz
    list->float'''
    denominador=0
    elementos=[]
    for sublista in matriz:
        for el in sublista:
            denominador= denominador+1
            elementos=elementos+[el]
    return (sum(elementos))/denominador