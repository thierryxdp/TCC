#Questão 5
def busca(setor, matriz):
    """Função que retorna as informações dos funcionários que
    estão no setor pesquisado;
    str, list -> list"""
    resultadosBusca = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor == matriz[i][j]:
                list.append(resultadosBusca, matriz[i])
                del resultadoBusca[i][2]
    return resultadosBusca