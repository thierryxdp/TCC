def posLetra(string,letra,n):
    '''funcao que recebe como entrada uma string,letra e um
    numero n que indica a ocorrencia desejada da letra e retorna
    a posicao da string onde aquela ocorrencia da letra esta
    str, str, int -> int'''
    proximo=0
    ocorrencia=0
    indice=0
    while proximo<len(string):
        if string[proximo]==letra:
            ocorrencia=ocorrencia+1
        indice= indice +1
        if ocorrencia==n:
            str.index(string,letra,indice)