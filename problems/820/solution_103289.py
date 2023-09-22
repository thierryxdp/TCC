def posLetra(frase, letra, n):
    '''retorna a posicao da ocorrencia n de uma letra na frase
    str, str, int -> int'''
    n=-1
    while pos>=0 and n>1:
        if letra!=frase:
        pos=str.find(letra, str.find(letra)+1)
        n=n-1
    return pos