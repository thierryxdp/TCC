def repetidos(listaNum):
    '''Essa funcao recebe uma lista de inteiros/flutuantes
       e compara com seu anterior. Caso sejam parecidos, soma-se
       numa variavel e quando acaba as analises, retorna-se a
       quantidade de vezes que o dois numeros seguidos se
       repetem.

       (list -> int)
    '''
    numRepeticoes = 0
    qntElementos = len(listaNum)
    cont = 1

    while cont < qntElementos:
        if listaNum[cont] == listaNum[cont-1]:
            numRepeticoes += 1
        cont += 1
    return numRepeticoes