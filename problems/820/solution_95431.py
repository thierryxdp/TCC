def posLetra(string, letra, n):
    '''funcao que dadas uma string, uma letra, e um numero de ocorrencias, retorna a posicao da ocorrencia da letra
    desejada
    string, string, int -> int '''
    contaocorren = 0
    posicao = 0
    while(contaocorren < n):
    	posicao = str.find(string, letra, posicao)
    return posicao