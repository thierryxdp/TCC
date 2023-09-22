def media_matriz(matriz):
    '''Função que calcula e retorna a media de
    todos os números de uma dada matriz com pre
    cisão de duas casas decimais
    list -> float'''
    soma = 0
    tamanho = 0
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
    resultado= soma/tamanho
    return round(resultado,2)