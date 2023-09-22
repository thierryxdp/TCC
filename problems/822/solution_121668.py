def repetidos(lista):
    """recebe uma lista de numeros e retorna
o numero de vezes que um elemento da lista é
igual ao elemento anterior"""
    i=0
    qnt = 0 #quantidade de repetição
    while i <= len(lista):
        if i+1 == len(lista): #iguala a fim de não dar erro quando chegar na ultima posicao
            return qnt
    
        if lista[i] == lista[i+1]: #verifica a repetição
            qnt = qnt + 1

        i = i + 1
    return qnt