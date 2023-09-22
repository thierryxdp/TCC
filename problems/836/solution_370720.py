#Questão 5
def busca(setor, matriz):
    """Função que retorna as informações dos funcionários que
    estão no setor pesquisado;
    str, list -> list"""
    resultadosBusca = []
    for i in range(len(matriz)):
        for j in range(len(matriz[2])):
            if setor == matriz[2][j]:
            	resultadosBusca = resultadosBusca + resultadosBusca[i][j]
    return resultadosBusca