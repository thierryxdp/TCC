def posLetra(frase, letra, x):
    '''Entre com uma frase, uma letra e um numero para ser retornado a posição
    que da ocorrencia desejada de acordo com o numero dado
    String, Char, Int -> Int'''
    i=0
    lista=()
    
    while i!=x:
        Pos = frase.index(letra)
        lista=lista+Pos
    i=i+1

    return lista[-1]