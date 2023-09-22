def posLetra(string, letra, n):
    '''funcao que dadas uma string, uma letra, e um numero de ocorrencias, retorna a posicao da ocorrencia da letra
    desejada
    string, string, int -> int '''
    contaocorren = 0
    posicao = 0
    indice = 0
    while(contaocorren < n):
        if(letra in string):
            indice = str.find(string, letra)
            posicao = str.find(string, letra, indice)
            contaocorren += 1
    return posicao