def repetidos(lista):
    '''
        Função que retorna a quantidade de vezes que um elemento da lista é igual ao elemento anterior;
        lista(int) => int
    '''
    qtd_repetidos = 0

    for i in range(1, len(lista)):
        if(lista[i-1] == lista[i]):
            qtd_repetidos += 1

    return qtd_repetidos