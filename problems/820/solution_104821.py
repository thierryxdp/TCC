def posLetra(string,letra,ocorrencia):
    '''funcao que retorna a posicao da ocorrencia de uma letra dentro de uma string str,str,int->int'''
    i = 0
    x = ''
    while len(string) >= i:
        if letra in string:
            if ocorrencia > str.count(string,letra):
                return -1
            else:
                return str.find(strign,letra,ocorrencia-1)
        i = i + 1