def busca(nome,matriz):
    ''' faz uma busca na matriz por setor e retorna os resultados encontrados
    matriz -> matriz'''
    contador=[]
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if nome in linha:
                contador += linha
            return contador
        	else:
                return []