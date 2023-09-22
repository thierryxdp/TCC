def media(matriz):
    """Função que soma todos os valores da matriz e retorna o valor da media da soma total pelo numero de linha/coluna.
    Parametros: lista-> float"""
    soma = 0
    tamanho = 0
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
    return round(soma/tamanho,2)