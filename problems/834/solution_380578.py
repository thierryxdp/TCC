def media_matriz(matriz):
    'Função que recebe uma matriz e retorna a média dos seus termos.'
    'list->float'

    lista=[]

    for linha in matriz:
        for numero in linha:
            lista=lista+[numero]

    return round((sum(lista)/len(lista)),2)