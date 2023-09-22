def media_matriz(matriz):
    '''Calcula e retorna a media dos numeros de uma matriz nao vazia
       parameters:
       matriz: Matriz inicial que sera calculada a media
       list->float'''
    lista=[]
    for i in range(len(matriz)):
        for matriz[i] in matriz:
            lista+=[sum(matriz[i])]
            i+=1
        return round(sum(lista)/(len(matriz)*len(matriz[0])), 2)