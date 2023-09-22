def repetidos(lista):
    '''Função que, dada uma lista de número, retorna o número de vezes que o número posterior é igual ao anterior.
    list --> int'''
    contagem = 0
    i = 0
    while i < len(lista)-1:
        if lista[i] == lista[i+1]:
            contagem = contagem + 1
        i = i + 1
    return contagem