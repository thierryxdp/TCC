def posLetra(string,letra,n):
    '''A função recebe de entrada uma string(frase), uma letra desejada na string e um número n que simboliza a ocorrência desejada da letra inserida de entrada, em ordem de posição ou seja 1 para a primeira ocia, 2 para a segunda etc.
    retorna então a posição da string com a qual a ocorrência se estabeleceu. str,str,int->int'''
    string1 = str.replace(string,letra,'+',n-1)
    return str.find(string1,letra)