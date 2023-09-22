#Questão 5
def busca(setor, matriz):
    """Função que retorna as informações dos funcionários que
    estão no setor pesquisado;
    str, list -> list"""

    resultadosFinal = []
    for i in range(len(matriz)):
        
        resultadosBusca = []
        for j in range(len(matriz[0])):
            if setor == matriz[i][j]:
                
                list.append(resultadosBusca, matriz[i][0])
                list.append(resultadosBusca, matriz[i][1])
                list.append(resultadosBusca, matriz[i][3])
        list.append(resultadosFinal, resultadosBusca)
        	else:
                return []
    return resultadosFinal