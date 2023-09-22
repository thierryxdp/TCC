def posLetra(frase,letra,ocorrencia):
    '''retorna a posicao em que a ocorrencia da
    letra fornecida aparece na frase; str, str, int -> int'''
    i=0
    n=0
    while i<len(frase) or n==ocorrencia:
        if frase[i]==letra:
            n=n+1
        
        elif i==(len(frase)-1) and n<ocorrencia:
            return -1
        i=i+1
    return i