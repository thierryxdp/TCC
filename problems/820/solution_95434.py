def posLetra(string, letra, n):
    '''funcao que dadas uma string, uma letra, e um numero de ocorrencias, retorna a posicao da ocorrencia da letra
    desejada
    string, string, int -> int '''
    contaocorren = 0
    i = 0
    posicao = 0
    while(i < len(string)):
        if(string[i] == letra):
            contaocorren += 1
            posicao = str.find(string, letra, i)
            i += 1
        else:
            i += 1
    if(contaocorren == n):
        return posicao
    else:
        return -1