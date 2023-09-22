def posLetra(frase, letra, num):
    """Funcao recebe una string, uma letra e um número e retorna em que posicao da string aquela ocorrencia da letra esta"""
    x=0
    count=0
    while x<len(frase) and count<num:
        if frase[x]==letra:
            count=count+1
        x=x+1
    if count==num:
        return x-1
    else:
        return -1