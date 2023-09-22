def faltante(lista_peca):
    '''
        recebe uma lista contendo a numeracao das pecas de um quebra cabeca
        com excessao de uma peca faltante, retorna o numero dessa peca que
        falta
        entrada: lista
        saida: inteiro
    '''
    chq = 0
    teste = 1
    num_pecas = len(lista_peca) + 1
    list.sort(lista_peca)
    while chq < num_pecas:
        if teste in lista_peca:
            teste = teste + 1
        else:
            return teste
        chq = chq + 1
    return teste