def posLetra (palavra,letra,num):
    '''Dado palavra, letra e a ocorrencia desejada da letra(num),
    retornará a posição da letra.(str,str,int => int)'''

    posicao = 0
    n = 0

    while posicao != num:
        if palavra[n] == letra:
            posicao = posicao + 1
            n = n + 1
        if len(palavra) == n:
            posicao = num
            n = n + 2

    return str.find(palavra,letra,n-1)