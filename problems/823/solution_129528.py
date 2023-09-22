def faltante(lista):
    '''Função que ajuda a encontrar a peça que está faltando. Faz isso a partir da
lista fornecida de tamanho N-1, a comparando a outra lista com N-1 inteiros, numerados
de 1 a N e identificando qual está faltando, que corresponderá a peça do quebra
cabeça que está em falta
    list -> int
    '''
    tamanho = len(lista)+1
    lista_certa = []
    corrente = 1
    contador = 0
    resposta = 0
    while corrente<=tamanho:
        lista_certa += [corrente]
        corrente += 1
    while contador < tamanho:
        if lista_certa[contador] not in lista:
            resposta += lista_certa[contador]
        contador += 1
    return resposta