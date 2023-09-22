def posLetra(string,letra,num):
    '''Funcao que recebe uma string, uma letra e um numero que indica a ocorrencia
desejada da letra [1 - primeira. 2 - segunda. etc]. Retorna em que posicao da string
a ocorrencia esta. Caso exista menos ocorrencia da letra do que a ocorrencia pedida,
retorna -1'''
    i = 0
    posicoes = []
    if str.count(string,letra) < num:
        return -1
    while i < len(string):
        if string[i] == letra:
            list.append(posicoes,i)
        i = i+1
    return posicoes[num-1]