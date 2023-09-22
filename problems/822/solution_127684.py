def repetidos(lista):
    '''Função que recebe uma lista de números e retorna o númro de vezes que um elemento da lista é igual ao elemento anterior;
    list,int->'''
    proximo = 0
    repeticao = 0
    while proximo<len(lista)-1:
        if lista[proximo+1]==lista[proximo]:
            repeticao = repeticao + 1
        proximo = proximo + 1
    return repeticao