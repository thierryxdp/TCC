def busca(setor, matriz):
	'''A seguinte função irá retornar os dados 
    de todos os funcionários determinando setor
    str--> list'''
    
    dados = []
    
    for i in range(len(matriz)):
        if setor in matriz[i]:
            dados.append(matriz[i])

    for j in range(len(dados)):
        if dados[j][2] == setor:
            del dados[j][2]
        

    return dados