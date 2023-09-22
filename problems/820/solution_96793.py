def posLetra(frase, letra, x):
    '''Entre com uma frase, uma letra e um numero para ser retornado a posição
    que da ocorrencia desejada de acordo com o numero dado
    String, Char, Int -> Int'''
    i=0
    c=0
    cont=()
    vazio=-1

    while i<len(frase):
        if letra in frase:
            y=frase.index(letra)
            cont=cont+(y, )
            c=c+1
        if c==x:
            return cont[-1]
    i=i+1
    
    if len(cont)<x:
        return vazio

    return cont