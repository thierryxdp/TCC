def busca(nome,matriz):
    ''' faz uma busca na matriz por setor e retorna os resultados encontrados
    matriz -> matriz'''
    contador=[]
    for linha in range(len(matriz)):
        if nome in matriz[linha][2]:
            contador.append([matriz[linha][0],matriz[linha][1],matriz[linha][3]])
    return contador