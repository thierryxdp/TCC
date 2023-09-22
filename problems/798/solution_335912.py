def freq_palavras(frase):
    resultado={}
    posicao=0
    frase=frase.split()
    for palavra in frase:
        if posicao<len(frase):
            palavra=frase[posicao:posicao+1]
            resultado[''.join(palavra)]=frase.count(''.join(palavra))
            posicao=posicao+1
    return resultado