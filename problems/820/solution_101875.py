def posLetra(string,letra,n):
    """retorna a posicao em que a ocorrencia, de numero n,
    de uma letra esta localizada na string de entrada
    str,str,int--.int"""
    count=0
    count2=0
    while count2<n:
        if string[count]==letra:
            count2=count2+1
        count=count+1
    return count-1