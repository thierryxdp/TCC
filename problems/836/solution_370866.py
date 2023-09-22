#Questão 5
def busca(setor, matriz):
    """Função que retorna as informações dos funcionários que
    estão no setor pesquisado;
    str, list -> list"""
    resultadosBusca = []
    for i in range(len(matriz)):
        list.remove(matriz[i][2])
        for j in range(len(matriz[0])):
            if setor == matriz[i][j]:
                list.append(resultadosBusca, matriz[i])
                
    return resultadosBusca