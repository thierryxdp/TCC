def posLetra(string,l,n):
    '''retorna a posiçao da ocorrencia da letra desejada na string. str,str,int->int'''
    if n <= string.count(l):
        return str.index(string,l,n)
    else:
        -1