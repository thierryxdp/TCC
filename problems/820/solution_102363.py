def posLetra(palavras,letra,ocorrencia):
    '''retorna a ocorrencia desejada da letra entre as palavras na str
    str,str,int --> int'''
    i=0
    n=0
    while i < len(palavras) and n < ocorrencia:
        if letra in palavras:
            indice_letra=str.find(palavras,letra)
            i=i+1
            n=n+1
        if letra not in palavras:
            indice_letra=-1
    return indice_letra