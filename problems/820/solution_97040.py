def posLetra(palavra,letra,num):
    '''retorna a posição da letra, dado a palavra
    e a ocorrencia desejada da letra(num). str,str,int->int'''
    posicao= 0
    n = 0
    while posicao != num:
        if palavra[n] == letra:
            posicao = posicao + 1
        n = n + 1
        if len(palavra) == n:
            posicao = num
            n = n - 1
    return str.find(palavra,letra,n)