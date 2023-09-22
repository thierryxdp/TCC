def posLetra(string,letra,n):
    """retorna a posicao em que a ocorrencia, de numero n,
    de uma letra esta localizada na string de entrada
    str,str,int--.int"""
    count=0
    while count<n:
        if string[count]==letra:
            count=count+1
    return string[letra]