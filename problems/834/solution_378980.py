def media_matriz(matriz):
    '''retorna a media de todos os numeros da matriz'''
    '''list -> int'''
    i=0
    linhas=len(matriz)
    colunas=len(matriz[i])
    lista=[]
    
    while i < linhas:
        soma=sum(matriz[i])
        media_linha=soma/colunas
        list.append(lista,media_linha)
        i=i+1
        
    soma_matriz=sum(lista)
    media= soma_matriz/linhas
    
    return media